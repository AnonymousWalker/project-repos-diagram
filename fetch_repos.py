#!/usr/bin/env python3
"""Fetch public repos from Bible-Translation-Tools and WycliffeAssociates."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORGS = [
    "Bible-Translation-Tools",
    "WycliffeAssociates",
]

OUT_FILE = Path(__file__).resolve().parent / "public-repos.json"
API_BASE = "https://api.github.com"


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "WA-repos-fetcher",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_json(url: str) -> tuple[object, dict[str, str]]:
    req = urllib.request.Request(url, headers=github_headers())
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return json.loads(body), headers
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {detail}") from exc


def next_page_url(link_header: str | None) -> str | None:
    if not link_header:
        return None
    # Link: <url>; rel="next", <url>; rel="last"
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' in section:
            start = section.find("<") + 1
            end = section.find(">")
            if start > 0 and end > start:
                return section[start:end]
    return None


def fetch_org_repos(org: str) -> list[dict]:
    url = f"{API_BASE}/orgs/{org}/repos?type=public&per_page=100&sort=full_name"
    repos: list[dict] = []
    while url:
        chunk, headers = fetch_json(url)
        if not isinstance(chunk, list):
            raise RuntimeError(f"Unexpected response for {org}: {type(chunk)}")
        repos.extend(chunk)
        url = next_page_url(headers.get("link"))

    items = []
    for repo in repos:
        desc = (repo.get("description") or "").strip()
        items.append(
            {
                "org": org,
                "name": repo["name"],
                "url": repo["html_url"],
                "default_branch": repo.get("default_branch") or "",
                "description": desc,
            }
        )
    return items


def main() -> None:
    all_repos: list[dict] = []
    for org in ORGS:
        print(f"Fetching {org}...")
        org_repos = fetch_org_repos(org)
        print(f"  {len(org_repos)} public repos")
        all_repos.extend(org_repos)

    all_repos.sort(key=lambda r: (r["org"].lower(), r["name"].lower()))

    payload = {"repos": all_repos}

    OUT_FILE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(all_repos)} repos to {OUT_FILE}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

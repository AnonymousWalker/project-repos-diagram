#!/usr/bin/env python3
"""Generate Mermaid architecture markdown for public WA/BTT repos.

Probes via shallow sparse git clones (avoids GitHub REST rate limits).

Examples:
  python generate_architecture_docs.py
  python generate_architecture_docs.py --changed-only
  python generate_architecture_docs.py --only Bible-Translation-Tools/BTT-Writer
  python generate_architecture_docs.py --only Org/A --only Org/B --force
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPOS_JSON = ROOT / "public-repos.json"
OUT_DIR = ROOT / "architecture"
CLONE_DIR = ROOT / "_clones"
SHA_CACHE = ROOT / "architecture" / ".sha-cache.json"
SKIP = {"Orature", "Fetcher"}  # hand-written docs already exist
DEFAULT_WORKERS = 8

EXT_LANG = {
    ".kt": "Kotlin",
    ".kts": "Kotlin",
    ".java": "Java",
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".jsx": "JavaScript",
    ".cs": "C#",
    ".fs": "F#",
    ".go": "Go",
    ".rs": "Rust",
    ".swift": "Swift",
    ".dart": "Dart",
    ".rb": "Ruby",
    ".php": "PHP",
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".h": "C",
    ".hpp": "C++",
    ".m": "Objective-C",
    ".mm": "Objective-C",
    ".scala": "Scala",
    ".groovy": "Groovy",
    ".sh": "Shell",
    ".ps1": "PowerShell",
    ".bat": "Batch",
    ".cmd": "Batch",
    ".sql": "SQL",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".vue": "Vue",
    ".svelte": "Svelte",
    ".xml": "XML",
    ".gradle": "Gradle",
    ".xslt": "XSLT",
    ".xsl": "XSLT",
    ".tf": "HCL",
    ".yml": "YAML",
    ".yaml": "YAML",
}

HAND_AUTHORED = [
    {
        "org": "Bible-Translation-Tools",
        "name": "Orature",
        "path": "Orature-architecture.md",
        "hand": True,
        "description": (
            "Orature, an application for creating Narrations and Translations of "
            "Audio Bibles, Books, Resources, Commentaries, etc."
        ),
    },
    {
        "org": "Bible-Translation-Tools",
        "name": "Fetcher",
        "path": "Fetcher-architecture.md",
        "hand": True,
        "description": "An app/library for downloading Scritpure Source Audio for Translation",
    },
]


def sanitize_filename(name: str) -> str:
    return re.sub(r"[^\w.\-]+", "_", name)


def repo_key(repo: dict) -> str:
    return f"{repo['org']}/{repo['name']}"


def doc_path_for(repo: dict) -> Path:
    return OUT_DIR / repo["org"] / f"{sanitize_filename(repo['name'])}-architecture.md"


def mermaid_safe(label: str) -> str:
    return (
        label.replace('"', "'")
        .replace("<", "")
        .replace(">", "")
        .replace("\n", " ")
        .replace("[", "(")
        .replace("]", ")")
        .replace("{", "(")
        .replace("}", ")")
    )


def run(
    cmd: list[str], cwd: Path | None = None, timeout: int = 180
) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )


def load_sha_cache(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def save_sha_cache(path: Path, cache: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(sorted(cache.items())), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def remote_default_sha(repo: dict) -> str | None:
    """Resolve current tip SHA of the repo default branch via ls-remote."""
    url = f"https://github.com/{repo['org']}/{repo['name']}.git"
    branch = repo["default_branch"]
    proc = run(["git", "ls-remote", url, f"refs/heads/{branch}"], timeout=60)
    if proc.returncode != 0:
        # fallback: HEAD
        proc = run(["git", "ls-remote", url, "HEAD"], timeout=60)
        if proc.returncode != 0 or not proc.stdout.strip():
            return None
    line = proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else ""
    if not line:
        return None
    return line.split()[0]


def ensure_clone(repo: dict) -> Path | None:
    org, name, branch = repo["org"], repo["name"], repo["default_branch"]
    dest = CLONE_DIR / org / name
    if dest.exists() and (dest / ".git").exists():
        # refresh to latest default branch tip
        fetch = run(
            ["git", "fetch", "--depth", "1", "origin", branch],
            cwd=dest,
            timeout=180,
        )
        if fetch.returncode == 0:
            run(["git", "checkout", "-f", "FETCH_HEAD"], cwd=dest, timeout=60)
            run(["git", "clean", "-fdx"], cwd=dest, timeout=60)
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest, ignore_errors=True)

    url = f"https://github.com/{org}/{name}.git"
    proc = run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            "--branch",
            branch,
            url,
            str(dest),
        ],
        timeout=240,
    )
    if proc.returncode != 0:
        if dest.exists():
            shutil.rmtree(dest, ignore_errors=True)
        proc = run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", url, str(dest)],
            timeout=240,
        )
        if proc.returncode != 0:
            print(f"  clone failed {org}/{name}: {proc.stderr[-400:]}")
            return None
    return dest


def list_root(repo_dir: Path) -> tuple[list[str], list[str]]:
    """List root entries from git tree (works with blobless sparse checkouts)."""
    dirs: list[str] = []
    files: list[str] = []
    type_proc = run(["git", "ls-tree", "HEAD"], cwd=repo_dir, timeout=60)
    if type_proc.returncode != 0:
        for p in repo_dir.iterdir():
            if p.name == ".git":
                continue
            (dirs if p.is_dir() else files).append(p.name)
        return sorted(dirs, key=str.lower), sorted(files, key=str.lower)

    for line in type_proc.stdout.splitlines():
        try:
            meta, name = line.split("\t", 1)
            obj_type = meta.split()[1]
        except ValueError:
            continue
        if obj_type == "tree":
            dirs.append(name)
        else:
            files.append(name)
    return sorted(dirs, key=str.lower), sorted(files, key=str.lower)


def language_counts(repo_dir: Path) -> dict[str, int]:
    proc = run(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=repo_dir, timeout=60)
    if proc.returncode != 0:
        return {}
    counter: Counter[str] = Counter()
    for line in proc.stdout.splitlines():
        path = line.strip()
        if not path or path.startswith("."):
            continue
        lang = EXT_LANG.get(Path(path).suffix.lower())
        if lang:
            counter[lang] += 1
    return dict(counter.most_common(12))


def read_readme(repo_dir: Path) -> str | None:
    for name in ("README.md", "README.MD", "readme.md", "README", "Readme.md"):
        p = repo_dir / name
        if p.is_file():
            try:
                return p.read_text(encoding="utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                return None
    for name in ("README.md", "README", "readme.md"):
        proc = run(["git", "show", f"HEAD:{name}"], cwd=repo_dir, timeout=30)
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout
    return None


def summarize_readme(text: str | None, max_chars: int = 600) -> str:
    if not text:
        return ""
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            if lines:
                break
            continue
        if s.startswith("#"):
            continue
        if s.startswith("![") or s.startswith("<"):
            continue
        if s.startswith("[!") or ("badge" in s.lower() and s.startswith("[")):
            continue
        lines.append(s)
        if sum(len(x) for x in lines) > max_chars:
            break
    summary = re.sub(r"\s+", " ", " ".join(lines)).strip()
    return summary[:max_chars]


def detect_stack(root_names: list[str], languages: dict[str, int]) -> dict:
    names = {n.lower() for n in root_names}
    top_lang = max(languages, key=languages.get) if languages else ""

    kind = "library"
    stack: list[str] = []

    if {"settings.gradle", "settings.gradle.kts", "build.gradle", "build.gradle.kts"} & names:
        stack.append("Gradle / JVM")
        kind = "jvm-app" if {"src", "app", "jvm", "common"} & names else "jvm-lib"
    if "pom.xml" in names:
        stack.append("Maven / JVM")
    if "package.json" in names:
        stack.append("Node.js")
        kind = (
            "web"
            if {"src", "public", "app", "pages", "next.config.js", "vite.config.ts"} & names
            else "node-lib"
        )
    if "cargo.toml" in names:
        stack.append("Rust")
        kind = "rust"
    if "go.mod" in names:
        stack.append("Go")
        kind = "go"
    if {"pyproject.toml", "setup.py", "requirements.txt", "Pipfile"} & names:
        stack.append("Python")
        kind = "python"
    if {"dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml"} & names:
        stack.append("Docker")
    if any(n.endswith(".csproj") or n.endswith(".sln") or n.endswith(".fsproj") for n in names):
        stack.append(".NET / C#")
        kind = "dotnet"
    if "pubspec.yaml" in names:
        stack.append("Flutter / Dart")
        kind = "flutter"
    if "android" in names or "androidmanifest.xml" in names:
        stack.append("Android")
    if "chart.yaml" in names or "charts" in names:
        stack.append("Helm")
    if not stack and top_lang:
        stack.append(top_lang)

    return {
        "kind": kind,
        "stack": stack or ["Unknown"],
        "top_language": top_lang or "Unknown",
    }


def build_diagrams(repo: dict, probe: dict) -> tuple[str, str, str]:
    name = mermaid_safe(repo["name"])
    desc = mermaid_safe(repo.get("description") or "No description on GitHub")
    stack = ", ".join(probe["stack"])
    modules = probe.get("root_dirs") or []
    files = probe.get("root_files") or []

    ctx_nodes = []
    for i, m in enumerate(modules[:12]):
        ctx_nodes.append(f'    M{i}["{mermaid_safe(m)}"]')
    if not ctx_nodes:
        for i, f in enumerate(files[:8]):
            ctx_nodes.append(f'    F{i}["{mermaid_safe(f)}"]')
    module_block = "\n".join(ctx_nodes) if ctx_nodes else '    Core["source"]'

    if modules:
        edges = "\n".join(f"  Users --> M{i}" for i in range(min(12, len(modules))))
    elif files:
        edges = "\n".join(f"  Users --> F{i}" for i in range(min(8, len(files))))
    else:
        edges = "  Users --> Core"

    system = f"""```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["{name}"]
{module_block}
  end

  subgraph meta["Project profile"]
    Stack["Stack: {mermaid_safe(stack)}"]
    Lang["Primary language: {mermaid_safe(probe['top_language'])}"]
  end

{edges}
  Users -.-> Stack
```"""

    layer_lines = [f'    D{i}["{mermaid_safe(d)}"]' for i, d in enumerate(modules[:15])]
    if not layer_lines:
        layer_lines = ['    Src["repository root"]']
    links = (
        "\n".join(f"  Root --> D{i}" for i in range(min(15, len(modules))))
        if modules
        else "  Root --> Src"
    )

    structure = f"""```mermaid
flowchart TB
  Root["{name}<br/>{mermaid_safe(desc)[:80]}"]

  subgraph structure["Top-level layout"]
{chr(10).join(layer_lines)}
  end

{links}
```"""

    kind = probe["kind"]
    if kind in ("jvm-app", "jvm-lib"):
        flow = f"""```mermaid
flowchart LR
  App["{name}"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```"""
    elif kind in ("web", "node-lib"):
        flow = f"""```mermaid
flowchart LR
  Client["Browser / client"] --> App["{name}"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```"""
    elif kind == "python":
        flow = f"""```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["{name} core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```"""
    elif kind == "dotnet":
        flow = f"""```mermaid
flowchart LR
  Host["Host / UI"] --> App["{name}"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```"""
    elif kind == "rust":
        flow = f"""```mermaid
flowchart LR
  Bin["Binary / WASM"] --> Crate["{name} crate"]
  Crate --> Deps["Cargo dependencies"]
```"""
    elif kind == "flutter":
        flow = f"""```mermaid
flowchart LR
  UI["Flutter UI"] --> App["{name}"]
  App --> Platform["iOS / Android / desktop"]
```"""
    elif kind == "go":
        flow = f"""```mermaid
flowchart LR
  Cmd["cmd / main"] --> App["{name}"]
  App --> Pkgs["Internal packages"]
  Pkgs --> Ext["External services"]
```"""
    else:
        flow = f"""```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["{name}"]
  Repo --> Artifacts["Libraries / tools / content"]
```"""

    return system, structure, flow


def render_markdown(repo: dict, probe: dict) -> str:
    name = repo["name"]
    url = repo["url"]
    org = repo["org"]
    branch = repo["default_branch"]
    desc = repo.get("description") or ""
    readme_summary = probe.get("readme_summary") or ""
    intro = readme_summary or desc or f"{name} is a public repository under {org}."

    system, structure, flow = build_diagrams(repo, probe)

    langs = probe.get("languages") or {}
    lang_rows = "\n".join(
        f"| {k} | {v:,} files |" for k, v in sorted(langs.items(), key=lambda x: -x[1])[:8]
    ) or "| — | — |"

    modules = probe.get("root_dirs") or []
    files = probe.get("root_files") or []
    layout = ""
    if modules:
        layout += "**Directories:** " + ", ".join(f"`{m}`" for m in modules[:25]) + "\n\n"
    if files:
        layout += "**Notable files:** " + ", ".join(f"`{f}`" for f in files[:20]) + "\n"

    notes = [
        f"| **Stack** | {', '.join(probe.get('stack') or ['Unknown'])} |",
        f"| **Default branch** | `{branch}` |",
        f"| **Org** | {org} |",
    ]

    return f"""# {name} architecture

[{org}/{name}]({url}) — {desc or "_no GitHub description_"}.

{intro}

## System context

{system}

## Repository structure

{structure}

{layout}

## Runtime / integration sketch

{flow}

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
{lang_rows}

## Design notes

| Topic | Detail |
|--------|--------|
{chr(10).join(notes)}

## Related

- Source: [{org}/{name}]({url})
- Branch analyzed: `{branch}`
"""


def probe_repo(repo: dict) -> dict | None:
    org, name = repo["org"], repo["name"]
    print(f"Probing {org}/{name}...")
    repo_dir = ensure_clone(repo)
    if repo_dir is None:
        return None

    root_dirs, root_files = list_root(repo_dir)
    languages = language_counts(repo_dir)
    readme = read_readme(repo_dir)
    stack_info = detect_stack(root_dirs + root_files, languages)

    return {
        **stack_info,
        "root_dirs": root_dirs,
        "root_files": root_files,
        "languages": languages,
        "readme_summary": summarize_readme(readme),
    }


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_index(all_repos: list[dict], written: int, failed: int) -> None:
    index_entries = list(HAND_AUTHORED)
    for repo in all_repos:
        if repo["name"] in SKIP:
            continue
        out = doc_path_for(repo)
        index_entries.append(
            {
                "org": repo["org"],
                "name": repo["name"],
                "path": str(out.relative_to(ROOT)).replace("\\", "/"),
                "hand": False,
                "description": repo.get("description") or "",
            }
        )

    by_org: dict[str, list] = {}
    for e in index_entries:
        by_org.setdefault(e["org"], []).append(e)

    generated = sum(1 for e in index_entries if not e.get("hand"))
    lines = [
        "# WA / BTT repository architecture index",
        "",
        "Architecture diagrams (Mermaid) for public repositories under "
        "[Bible-Translation-Tools](https://github.com/Bible-Translation-Tools/) and "
        "[WycliffeAssociates](https://github.com/WycliffeAssociates/).",
        "",
        "- Hand-authored (deeper review): Orature, Fetcher",
        f"- Generated from repo layout/README: {generated}",
        f"- Last generation — wrote/updated: {written}, failed probes: {failed}",
        "",
    ]
    for org, entries in sorted(by_org.items()):
        lines.append(f"## {org}")
        lines.append("")
        for e in sorted(entries, key=lambda x: x["name"].lower()):
            tag = " *(hand-authored)*" if e.get("hand") else ""
            desc = e.get("description") or ""
            suffix = f" — {desc}" if desc else ""
            lines.append(f"- [{e['name']}]({e['path']}){tag}{suffix}")
        lines.append("")

    (ROOT / "architecture-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="ORG/REPO",
        help="Only process this repo (repeatable). Example: --only Bible-Translation-Tools/Orature",
    )
    p.add_argument(
        "--changed-only",
        action="store_true",
        help="Only regenerate repos whose default-branch SHA changed vs the SHA cache",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Regenerate even if remote SHA matches cache",
    )
    p.add_argument(
        "--sha-cache",
        type=Path,
        default=SHA_CACHE,
        help=f"Path to SHA cache JSON (default: {SHA_CACHE})",
    )
    p.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Parallel clone/probe workers (default: {DEFAULT_WORKERS})",
    )
    p.add_argument(
        "--refresh-index-only",
        action="store_true",
        help="Only rebuild architecture-index.md from public-repos.json + existing docs",
    )
    return p.parse_args()


def select_repos(all_repos: list[dict], args: argparse.Namespace, cache: dict[str, str]) -> list[dict]:
    repos = [r for r in all_repos if r["name"] not in SKIP]

    if args.only:
        wanted = {item.strip().lower() for item in args.only}
        repos = [r for r in repos if repo_key(r).lower() in wanted]
        missing = wanted - {repo_key(r).lower() for r in repos}
        # allow targeting skipped hand-authored names only if explicitly requested? keep skip
        for m in sorted(missing):
            print(f"Warning: --only {m} not found in public-repos.json (or is hand-authored skip)")

    if args.changed_only and not args.force:
        changed: list[dict] = []
        for repo in repos:
            key = repo_key(repo)
            sha = remote_default_sha(repo)
            if sha is None:
                print(f"  could not resolve SHA for {key}; will regenerate")
                changed.append(repo)
                continue
            if cache.get(key) != sha:
                print(f"  changed: {key} ({cache.get(key, 'none')[:7] if cache.get(key) else 'none'} -> {sha[:7]})")
                changed.append(repo)
            else:
                print(f"  unchanged: {key}")
        repos = changed

    return repos


def main() -> None:
    args = parse_args()
    data = json.loads(REPOS_JSON.read_text(encoding="utf-8"))
    all_repos: list[dict] = data["repos"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CLONE_DIR.mkdir(parents=True, exist_ok=True)

    cache = load_sha_cache(args.sha_cache)

    if args.refresh_index_only:
        write_index(all_repos, written=0, failed=0)
        print("Rebuilt architecture-index.md")
        return

    repos = select_repos(all_repos, args, cache)
    if not repos:
        print("Nothing to regenerate.")
        write_index(all_repos, written=0, failed=0)
        return

    print(f"Generating architecture docs for {len(repos)} repos (workers={args.workers})")
    started = time.time()
    results: list[tuple[dict, dict | None, str | None]] = []

    def work(repo: dict):
        sha = remote_default_sha(repo)
        try:
            return repo, probe_repo(repo), sha
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED {repo['org']}/{repo['name']}: {exc}")
            return repo, None, sha

    workers = max(1, args.workers)
    if workers == 1 or len(repos) == 1:
        for repo in repos:
            results.append(work(repo))
    else:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [ex.submit(work, r) for r in repos]
            for fut in as_completed(futs):
                results.append(fut.result())

    results.sort(key=lambda t: (t[0]["org"].lower(), t[0]["name"].lower()))

    written = 0
    failed = 0
    updated_files = 0
    for repo, probe, sha in results:
        if probe is None:
            failed += 1
            probe = {
                "kind": "unknown",
                "stack": ["Unknown"],
                "top_language": "Unknown",
                "root_dirs": [],
                "root_files": [],
                "languages": {},
                "readme_summary": "",
            }
        org_dir = OUT_DIR / repo["org"]
        org_dir.mkdir(parents=True, exist_ok=True)
        out = doc_path_for(repo)
        markdown = render_markdown(repo, probe)
        prev = out.read_text(encoding="utf-8") if out.exists() else None
        if prev is None or content_hash(prev) != content_hash(markdown):
            out.write_text(markdown, encoding="utf-8")
            updated_files += 1
        written += 1
        if sha:
            cache[repo_key(repo)] = sha

    save_sha_cache(args.sha_cache, cache)
    write_index(all_repos, written=written, failed=failed)

    elapsed = time.time() - started
    print(
        f"Done in {elapsed:.1f}s. Processed {written}; markdown updated {updated_files}; "
        f"failed={failed}"
    )
    print(f"Index: {ROOT / 'architecture-index.md'}")
    print(f"SHA cache: {args.sha_cache}")
    print(f"Clones kept under: {CLONE_DIR}")


if __name__ == "__main__":
    main()

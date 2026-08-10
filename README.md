# Project repos diagram

Mermaid architecture diagrams for public repositories under:

- [Bible-Translation-Tools](https://github.com/Bible-Translation-Tools/)
- [WycliffeAssociates](https://github.com/WycliffeAssociates/)

Start here: **[architecture-index.md](architecture-index.md)** · Viewer: **`front-end/`** (`pnpm --dir front-end dev`)

## Layout

| Path | Purpose |
|------|---------|
| `public-repos.json` | Catalog of public repos (name, url, default branch, description) |
| `architecture/{org}/{repo}-architecture.md` | Generated diagrams |
| `Orature-architecture.md` / `Fetcher-architecture.md` | Hand-authored deep reviews |
| `architecture/.sha-cache.json` | Default-branch SHAs used for incremental regen |
| `fetch_repos.py` | Refresh `public-repos.json` from GitHub |
| `generate_architecture_docs.py` | Probe repos and render Mermaid markdown |
| `front-end/` | Web app to browse/render markdown + Mermaid (pan/zoom) |

## Local usage

```bash
# Refresh catalog
python fetch_repos.py

# Full generate
python generate_architecture_docs.py --force

# Only repos whose default branch moved
python generate_architecture_docs.py --changed-only

# Single repo
python generate_architecture_docs.py --only Bible-Translation-Tools/BTT-Writer --force

# Browse diagrams in the web viewer
pnpm --dir front-end install
pnpm --dir front-end dev
```

Clones are stored under `_clones/` (gitignored).

## CI pipeline

GitHub Actions workflow [`.github/workflows/regenerate-architecture.yml`](.github/workflows/regenerate-architecture.yml):

1. **Schedule** — twice daily (`06:00` and `18:00` UTC), regenerate `--changed-only`
2. **workflow_dispatch** — manual `changed-only` or `full`, optional `Org/Repo`
3. **repository_dispatch** — type `repo-default-branch-changed` with payload `{ "repo": "Org/Name" }` for future webhooks

On changes, the workflow commits and pushes updated diagrams.

### Optional near-real-time hook

Point org webhooks (or a small relay) at:

```http
POST /repos/AnonymousWalker/project-repos-diagram/dispatches
```

with:

```json
{
  "event_type": "repo-default-branch-changed",
  "client_payload": { "repo": "Bible-Translation-Tools/SomeRepo" }
}
```

## Notes

- Orature and Fetcher are skipped by the generator so hand-authored docs are not overwritten.
- Generated diagrams are inferred from layout/README; treat them as maps, not design reviews.

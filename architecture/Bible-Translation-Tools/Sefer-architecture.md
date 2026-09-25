# Sefer architecture

[Bible-Translation-Tools/Sefer](https://github.com/Bible-Translation-Tools/Sefer) — An editor for usfm scripture.

Sefer is a local-first scripture editor. Its editing authority is one canonical UTF-8 Source per Book; parser products, diagnostics, and rendered views are derived from that Source.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Sefer"]
    M0[".claude"]
    M1[".github"]
    M2[".zed"]
    M3["agents"]
    M4["documentation"]
    M5["e2e"]
    M6["fixtures"]
    M7["planning"]
    M8["public"]
    M9["src"]
    M10["src-tauri"]
    M11["tools"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users --> M10
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Sefer<br/>An editor for usfm scripture"]

  subgraph structure["Top-level layout"]
    D0[".claude"]
    D1[".github"]
    D2[".zed"]
    D3["agents"]
    D4["documentation"]
    D5["e2e"]
    D6["fixtures"]
    D7["planning"]
    D8["public"]
    D9["src"]
    D10["src-tauri"]
    D11["tools"]
    D12["workers"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
  Root --> D9
  Root --> D10
  Root --> D11
  Root --> D12
```

**Directories:** `.claude`, `.github`, `.zed`, `agents`, `documentation`, `e2e`, `fixtures`, `planning`, `public`, `src`, `src-tauri`, `tools`, `workers`

**Notable files:** `.fallowrc.jsonc`, `.gitignore`, `.oxfmtrc.json`, `AGENTS.md`, `CLAUDE.MD`, `lefthook.yml`, `oxlint.config.ts`, `oxlint.release.config.ts`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `README.md`, `tsconfig.json`, `vite.config.ts`, `wrangler.jsonc`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["Sefer"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 357 files |
| Rust | 7 files |
| YAML | 4 files |
| CSS | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Sefer](https://github.com/Bible-Translation-Tools/Sefer)
- Branch analyzed: `master`

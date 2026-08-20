# Transcriber architecture

[Bible-Translation-Tools/Transcriber](https://github.com/Bible-Translation-Tools/Transcriber) — _no GitHub description_.

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Transcriber"]
    M0[".vscode"]
    M1["drizzle"]
    M2["public"]
    M3["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Transcriber<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".vscode"]
    D1["drizzle"]
    D2["public"]
    D3["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.vscode`, `drizzle`, `public`, `src`

**Notable files:** `.gitignore`, `biome.jsonc`, `crowdin.yml`, `drizzle.config.ts`, `index.html`, `lefthook.yml`, `LICENSE`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `README.md`, `tsconfig.app.json`, `tsconfig.json`, `tsconfig.node.json`, `tsconfig.worker.json`, `vite.config.ts`, `worker-configuration.d.ts`, `wrangler.jsonc`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["Transcriber"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 84 files |
| YAML | 4 files |
| SQL | 3 files |
| CSS | 3 files |
| HTML | 1 files |
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `default` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Transcriber](https://github.com/Bible-Translation-Tools/Transcriber)
- Branch analyzed: `default`

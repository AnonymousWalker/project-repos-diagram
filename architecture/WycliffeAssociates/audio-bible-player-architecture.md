# audio-bible-player architecture

[WycliffeAssociates/audio-bible-player](https://github.com/WycliffeAssociates/audio-bible-player) — _no GitHub description_.

audio-bible-player is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["audio-bible-player"]
    M0[".github"]
    M1[".vscode"]
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
  Root["audio-bible-player<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["public"]
    D3["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `.vscode`, `public`, `src`

**Notable files:** `.gitignore`, `astro.config.ts`, `package.json`, `pnpm-lock.yaml`, `README.md`, `tsconfig.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["audio-bible-player"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 13 files |
| YAML | 1 files |
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `prod` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/audio-bible-player](https://github.com/WycliffeAssociates/audio-bible-player)
- Branch analyzed: `prod`

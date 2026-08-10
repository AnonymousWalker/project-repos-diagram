# BIEL-mobile-app architecture

[Bible-Translation-Tools/BIEL-mobile-app](https://github.com/Bible-Translation-Tools/BIEL-mobile-app) — _no GitHub description_.

Expo (SDK 55) app using [Expo Router](https://docs.expo.dev/router/introduction/) with routes in `src/app/`.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BIEL-mobile-app"]
    M0[".claude"]
    M1[".github"]
    M2[".vscode"]
    M3["assets"]
    M4["docs"]
    M5["patches"]
    M6["plugins"]
    M7["scripts"]
    M8["src"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["BIEL-mobile-app<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".claude"]
    D1[".github"]
    D2[".vscode"]
    D3["assets"]
    D4["docs"]
    D5["patches"]
    D6["plugins"]
    D7["scripts"]
    D8["src"]
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
```

**Directories:** `.claude`, `.github`, `.vscode`, `assets`, `docs`, `patches`, `plugins`, `scripts`, `src`

**Notable files:** `.gitignore`, `.npmrc`, `app.json`, `eslint.config.js`, `index.js`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `README.md`, `tsconfig.json`, `vitest.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["BIEL-mobile-app"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 141 files |
| JavaScript | 5 files |
| YAML | 2 files |
| HTML | 2 files |
| CSS | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BIEL-mobile-app](https://github.com/Bible-Translation-Tools/BIEL-mobile-app)
- Branch analyzed: `main`

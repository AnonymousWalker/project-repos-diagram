# DOT-mobile architecture

[WycliffeAssociates/DOT-mobile](https://github.com/WycliffeAssociates/DOT-mobile) — _no GitHub description_.

DOT-mobile is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["DOT-mobile"]
    M0[".github"]
    M1[".husky"]
    M2[".vscode"]
    M3["android"]
    M4["assets"]
    M5["icons"]
    M6["ios"]
    M7["public"]
    M8["src"]
    M9["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Android"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["DOT-mobile<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".husky"]
    D2[".vscode"]
    D3["android"]
    D4["assets"]
    D5["icons"]
    D6["ios"]
    D7["public"]
    D8["src"]
    D9["tests"]
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
```

**Directories:** `.github`, `.husky`, `.vscode`, `android`, `assets`, `icons`, `ios`, `public`, `src`, `tests`

**Notable files:** `.browserslistrc`, `.eslintrc.cjs`, `.gitignore`, `biome.json`, `capacitor.config.ts`, `eslint.config.js`, `index.html`, `ionic.config.json`, `package-lock.json`, `package.json`, `playwright.config.ts`, `tsconfig.json`, `tsconfig.node.json`, `uno.config.ts`, `vite.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["DOT-mobile"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 31 files |
| XML | 10 files |
| Gradle | 6 files |
| CSS | 4 files |
| Java | 3 files |
| JavaScript | 2 files |
| Batch | 1 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Android |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/DOT-mobile](https://github.com/WycliffeAssociates/DOT-mobile)
- Branch analyzed: `master`

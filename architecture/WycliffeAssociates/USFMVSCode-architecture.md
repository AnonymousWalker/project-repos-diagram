# USFMVSCode architecture

[WycliffeAssociates/USFMVSCode](https://github.com/WycliffeAssociates/USFMVSCode) — Visual Studio Code plugin for USFM Support.

A Visual Studio Code Plugin to provide support for USFM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMVSCode"]
    M0[".github"]
    M1[".vscode"]
    M2["src"]
    M3["syntaxes"]
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
  Root["USFMVSCode<br/>Visual Studio Code plugin for USFM Support"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["src"]
    D3["syntaxes"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `.vscode`, `src`, `syntaxes`

**Notable files:** `.eslintrc.json`, `.gitattributes`, `.gitignore`, `.vscodeignore`, `CHANGELOG.md`, `LICENSE`, `package-lock.json`, `package.json`, `README.md`, `tsconfig.json`, `webpack.config.js`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["USFMVSCode"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 13 files |
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMVSCode](https://github.com/WycliffeAssociates/USFMVSCode)
- Branch analyzed: `master`

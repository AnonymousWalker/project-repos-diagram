# basic-tools-site architecture

[WycliffeAssociates/basic-tools-site](https://github.com/WycliffeAssociates/basic-tools-site) — _no GitHub description_.

basic-tools-site is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["basic-tools-site"]
    M0[".github"]
    M1[".vscode"]
    M2["functions"]
    M3["web-app"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
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
  Root["basic-tools-site<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["functions"]
    D3["web-app"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `.vscode`, `functions`, `web-app`

**Notable files:** `.funcignore`, `.gitignore`, `host.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["basic-tools-site"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 2 files |
| CSS | 1 files |
| HTML | 1 files |
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/basic-tools-site](https://github.com/WycliffeAssociates/basic-tools-site)
- Branch analyzed: `master`

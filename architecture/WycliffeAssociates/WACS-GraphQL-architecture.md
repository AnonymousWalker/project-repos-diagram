# WACS-GraphQL architecture

[WycliffeAssociates/WACS-GraphQL](https://github.com/WycliffeAssociates/WACS-GraphQL) — _no GitHub description_.

WACS-GraphQL is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["WACS-GraphQL"]
    M0[".github"]
    M1[".vscode"]
    M2["WACS_GraphQL"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["WACS-GraphQL<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["WACS_GraphQL"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `.vscode`, `WACS_GraphQL`

**Notable files:** `.funcignore`, `.gitignore`, `getting_started.md`, `host.json`, `makefile`, `requirements.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["WACS-GraphQL core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/WACS-GraphQL](https://github.com/WycliffeAssociates/WACS-GraphQL)
- Branch analyzed: `main`

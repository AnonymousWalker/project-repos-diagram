# gogs-custom architecture

[WycliffeAssociates/gogs-custom](https://github.com/WycliffeAssociates/gogs-custom) — Gitea customizations.

This project is UI customizations for WA's Gitea instance. The files here were forked from [Gitea](https://github.com/go-gitea/gitea) and [Gogs](https://gogs.io).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["gogs-custom"]
    M0[".github"]
    M1["assets"]
    M2["options"]
    M3["public"]
    M4["templates"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["gogs-custom<br/>Gitea customizations"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["assets"]
    D2["options"]
    D3["public"]
    D4["templates"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.github`, `assets`, `options`, `public`, `templates`

**Notable files:** `.editorconfig`, `.gitattributes`, `.gitignore`, `DCO`, `LICENSE`, `makecss.sh`, `package.json`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["gogs-custom"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 176 files |
| HTML | 133 files |
| CSS | 16 files |
| Shell | 1 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `content.bibletranslationtools.org` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/gogs-custom](https://github.com/WycliffeAssociates/gogs-custom)
- Branch analyzed: `content.bibletranslationtools.org`

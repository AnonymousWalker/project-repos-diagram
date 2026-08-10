# wacs-docker architecture

[WycliffeAssociates/wacs-docker](https://github.com/WycliffeAssociates/wacs-docker) — _no GitHub description_.

This project is UI customizations for WA's Gitea instance. The files here were forked from [Gitea](https://github.com/go-gitea/gitea) and [Gogs](https://gogs.io).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["wacs-docker"]
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
  Root["wacs-docker<br/>No description on GitHub"]

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
  Client["Browser / client"] --> App["wacs-docker"]
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
| **Default branch** | `content-dev.bibletranslationtools.org` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/wacs-docker](https://github.com/WycliffeAssociates/wacs-docker)
- Branch analyzed: `content-dev.bibletranslationtools.org`

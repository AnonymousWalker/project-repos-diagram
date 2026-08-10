# scripture-sous-chef architecture

[WycliffeAssociates/scripture-sous-chef](https://github.com/WycliffeAssociates/scripture-sous-chef) — A library for statistical anomaly detection and hygiene for usfm scripture projects..

A pure, addressable **content analyzer** for scripture text. It receives the plain text of each verse and returns **ranges** — spellcheck-style findings ("there are two spaces here," control characters, …) — that an editor can resolve to highlights. Aimed at field Bible translators working in low-resource majority-world languages.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["scripture-sous-chef"]
    M0[".codegraph"]
    M1["crates"]
    M2["documentation"]
    M3["pkg-bundler"]
    M4["pkg-web"]
    M5["scripts"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Rust"]
    Lang["Primary language: Rust"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-sous-chef<br/>A library for statistical anomaly detection and hygiene for usfm scripture proje"]

  subgraph structure["Top-level layout"]
    D0[".codegraph"]
    D1["crates"]
    D2["documentation"]
    D3["pkg-bundler"]
    D4["pkg-web"]
    D5["scripts"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.codegraph`, `crates`, `documentation`, `pkg-bundler`, `pkg-web`, `scripts`

**Notable files:** `.DS_Store`, `.gitignore`, `Cargo.lock`, `Cargo.toml`, `package.json`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Bin["Binary / WASM"] --> Crate["scripture-sous-chef crate"]
  Crate --> Deps["Cargo dependencies"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Rust | 20 files |
| TypeScript | 4 files |
| JavaScript | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-sous-chef](https://github.com/WycliffeAssociates/scripture-sous-chef)
- Branch analyzed: `master`

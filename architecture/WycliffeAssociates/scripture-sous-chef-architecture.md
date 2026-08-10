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
    M0[".cargo"]
    M1[".claude"]
    M2[".codegraph"]
    M3["crates"]
    M4["documentation"]
    M5["pkg-bundler"]
    M6["pkg-web"]
    M7["scripts"]
    M8["spike-bench"]
    M9["xtask"]
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
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-sous-chef<br/>A library for statistical anomaly detection and hygiene for usfm scripture proje"]

  subgraph structure["Top-level layout"]
    D0[".cargo"]
    D1[".claude"]
    D2[".codegraph"]
    D3["crates"]
    D4["documentation"]
    D5["pkg-bundler"]
    D6["pkg-web"]
    D7["scripts"]
    D8["spike-bench"]
    D9["xtask"]
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

**Directories:** `.cargo`, `.claude`, `.codegraph`, `crates`, `documentation`, `pkg-bundler`, `pkg-web`, `scripts`, `spike-bench`, `xtask`

**Notable files:** `.gitignore`, `Cargo.lock`, `Cargo.toml`, `CLAUDE.md`, `clippy.toml`, `glossary.md`, `package.json`, `README.md`


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
| Rust | 97 files |
| TypeScript | 10 files |
| JavaScript | 9 files |
| HTML | 3 files |
| Shell | 2 files |
| Python | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-sous-chef](https://github.com/WycliffeAssociates/scripture-sous-chef)
- Branch analyzed: `master`

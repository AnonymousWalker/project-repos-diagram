# scripture-kitchen architecture

[WycliffeAssociates/scripture-kitchen](https://github.com/WycliffeAssociates/scripture-kitchen) — Tools for slicing, dicing, and stewing up up some usfm..

A USFM engine in Rust: lex, CST, lint, format, and the USJ / USX / HTML exports, plus a JS doorway over the same code.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["scripture-kitchen"]
    M0[".github"]
    M1["corpora"]
    M2["docs"]
    M3["galley"]
    M4["mise"]
    M5["onion"]
    M6["onion-wasm"]
    M7["planning"]
    M8["sous-chef"]
    M9["tcdocs"]
    M10["testData"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Rust"]
    Lang["Primary language: XML"]
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
  Users --> M10
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-kitchen<br/>Tools for slicing, dicing, and stewing up up some usfm."]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["corpora"]
    D2["docs"]
    D3["galley"]
    D4["mise"]
    D5["onion"]
    D6["onion-wasm"]
    D7["planning"]
    D8["sous-chef"]
    D9["tcdocs"]
    D10["testData"]
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
  Root --> D10
```

**Directories:** `.github`, `corpora`, `docs`, `galley`, `mise`, `onion`, `onion-wasm`, `planning`, `sous-chef`, `tcdocs`, `testData`

**Notable files:** `.gitignore`, `Cargo.lock`, `Cargo.toml`, `CLAUDE.md`, `clippy.toml`, `GLOSSARY.md`, `package.json`, `README.md`, `rust-toolchain.toml`


## Runtime / integration sketch

```mermaid
flowchart LR
  Bin["Binary / WASM"] --> Crate["scripture-kitchen crate"]
  Crate --> Deps["Cargo dependencies"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 522 files |
| Rust | 111 files |
| TypeScript | 7 files |
| YAML | 6 files |
| JavaScript | 3 files |
| Shell | 2 files |
| Python | 2 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-kitchen](https://github.com/WycliffeAssociates/scripture-kitchen)
- Branch analyzed: `master`

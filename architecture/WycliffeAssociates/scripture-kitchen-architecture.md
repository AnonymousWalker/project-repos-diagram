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
    M1["docs"]
    M2["galley"]
    M3["onion"]
    M4["onion-wasm"]
    M5["planning"]
    M6["tcdocs"]
    M7["testData"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-kitchen<br/>Tools for slicing, dicing, and stewing up up some usfm."]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["docs"]
    D2["galley"]
    D3["onion"]
    D4["onion-wasm"]
    D5["planning"]
    D6["tcdocs"]
    D7["testData"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
```

**Directories:** `.github`, `docs`, `galley`, `onion`, `onion-wasm`, `planning`, `tcdocs`, `testData`

**Notable files:** `.gitignore`, `Cargo.lock`, `Cargo.toml`, `CLAUDE.md`, `GLOSSARY.md`, `package.json`, `README.md`, `rust-toolchain.toml`


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
| Rust | 75 files |
| TypeScript | 6 files |
| YAML | 6 files |
| JavaScript | 3 files |
| Python | 2 files |
| HTML | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-kitchen](https://github.com/WycliffeAssociates/scripture-kitchen)
- Branch analyzed: `master`

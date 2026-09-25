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
    M1["agents"]
    M2["corpora"]
    M3["docs"]
    M4["galley"]
    M5["mise"]
    M6["onion"]
    M7["onion-wasm"]
    M8["planning"]
    M9["sous-chef"]
    M10["tcdocs"]
    M11["testData"]
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
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-kitchen<br/>Tools for slicing, dicing, and stewing up up some usfm."]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["agents"]
    D2["corpora"]
    D3["docs"]
    D4["galley"]
    D5["mise"]
    D6["onion"]
    D7["onion-wasm"]
    D8["planning"]
    D9["sous-chef"]
    D10["tcdocs"]
    D11["testData"]
    D12["ticket"]
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
  Root --> D11
  Root --> D12
```

**Directories:** `.github`, `agents`, `corpora`, `docs`, `galley`, `mise`, `onion`, `onion-wasm`, `planning`, `sous-chef`, `tcdocs`, `testData`, `ticket`

**Notable files:** `.gitignore`, `.mbx.toml`, `Cargo.lock`, `Cargo.toml`, `CLAUDE.md`, `clippy.toml`, `GLOSSARY.md`, `package-root.mjs`, `package.json`, `README.md`, `rust-toolchain.toml`, `wasm-build.sh`


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
| Rust | 234 files |
| TypeScript | 15 files |
| JavaScript | 6 files |
| YAML | 6 files |
| Shell | 4 files |
| HTML | 2 files |
| Python | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-kitchen](https://github.com/WycliffeAssociates/scripture-kitchen)
- Branch analyzed: `master`

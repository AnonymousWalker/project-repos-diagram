# symbolic architecture

[WycliffeAssociates/symbolic](https://github.com/WycliffeAssociates/symbolic) — Stack trace symbolication library written in Rust.

Symbolic is a library written in Rust which is used at [Sentry](https://sentry.io/) to implement symbolication of native stack traces, sourcemap handling for minified JavaScript and more. It consists of multiple largely independent crates which are bundled together into a C and Python library so it can be used independently of Rust.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["symbolic"]
    M0[".github"]
    M1[".vscode"]
    M2["cabi"]
    M3["common"]
    M4["debuginfo"]
    M5["demangle"]
    M6["examples"]
    M7["minidump"]
    M8["proguard"]
    M9["py"]
    M10["scripts"]
    M11["sourcemap"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Rust"]
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
  Users --> M10
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["symbolic<br/>Stack trace symbolication library written in Rust"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["cabi"]
    D3["common"]
    D4["debuginfo"]
    D5["demangle"]
    D6["examples"]
    D7["minidump"]
    D8["proguard"]
    D9["py"]
    D10["scripts"]
    D11["sourcemap"]
    D12["src"]
    D13["symcache"]
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
  Root --> D13
```

**Directories:** `.github`, `.vscode`, `cabi`, `common`, `debuginfo`, `demangle`, `examples`, `minidump`, `proguard`, `py`, `scripts`, `sourcemap`, `src`, `symcache`

**Notable files:** `.clang-format`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.gitmodules`, `.travis.yml`, `Cargo.toml`, `LICENSE`, `Makefile`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Bin["Binary / WASM"] --> Crate["symbolic crate"]
  Crate --> Deps["Cargo dependencies"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Rust | 51 files |
| C | 31 files |
| Python | 21 files |
| JavaScript | 19 files |
| C++ | 14 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/symbolic](https://github.com/WycliffeAssociates/symbolic)
- Branch analyzed: `master`

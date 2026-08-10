# usfm-onion architecture

[WycliffeAssociates/usfm-onion](https://github.com/WycliffeAssociates/usfm-onion) — A toolkit for working with usfm in rust and wasm.

`usfm_onion` is a Rust-first USFM engine built around one canonical working model: flat tokens.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["usfm-onion"]
    M0[".cargo"]
    M1["benches"]
    M2["crates"]
    M3["docs"]
    M4["example-corpora"]
    M5["examples"]
    M6["js"]
    M7["pkg-bundler"]
    M8["pkg-web"]
    M9["plans"]
    M10["proptest-regressions"]
    M11["scripts"]
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
  Root["usfm-onion<br/>A toolkit for working with usfm in rust and wasm"]

  subgraph structure["Top-level layout"]
    D0[".cargo"]
    D1["benches"]
    D2["crates"]
    D3["docs"]
    D4["example-corpora"]
    D5["examples"]
    D6["js"]
    D7["pkg-bundler"]
    D8["pkg-web"]
    D9["plans"]
    D10["proptest-regressions"]
    D11["scripts"]
    D12["src"]
    D13["testData"]
    D14["tests"]
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
  Root --> D14
```

**Directories:** `.cargo`, `benches`, `crates`, `docs`, `example-corpora`, `examples`, `js`, `pkg-bundler`, `pkg-web`, `plans`, `proptest-regressions`, `scripts`, `src`, `testData`, `tests`

**Notable files:** `.gitattributes`, `.gitignore`, `BENCH_RESULTS.md`, `BENCH_RESULTS_WASM.md`, `Cargo.lock`, `Cargo.toml`, `CLAUDE.md`, `clippy.toml`, `package-lock.json`, `package.json`, `perf-notes.md`, `README.md`, `tsconfig.packed-fixture.json`, `vision.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Bin["Binary / WASM"] --> Crate["usfm-onion crate"]
  Crate --> Deps["Cargo dependencies"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 529 files |
| Rust | 95 files |
| HTML | 15 files |
| TypeScript | 8 files |
| YAML | 6 files |
| JavaScript | 6 files |
| Python | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Rust |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/usfm-onion](https://github.com/WycliffeAssociates/usfm-onion)
- Branch analyzed: `master`

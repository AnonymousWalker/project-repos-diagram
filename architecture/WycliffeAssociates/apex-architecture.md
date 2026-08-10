# apex architecture

[WycliffeAssociates/apex](https://github.com/WycliffeAssociates/apex) — Old apex/apex.

This software is no longer being maintainted and should not be chosen for new projects. See this [issue](https://github.com/apex/apex/issues/932) for more information

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["apex"]
    M0[".github"]
    M1["_examples"]
    M2["archive"]
    M3["assets"]
    M4["boot"]
    M5["cmd"]
    M6["colors"]
    M7["cost"]
    M8["docs"]
    M9["dryrun"]
    M10["exec"]
    M11["function"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Go"]
    Lang["Primary language: Go"]
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
  Root["apex<br/>Old apex/apex"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["_examples"]
    D2["archive"]
    D3["assets"]
    D4["boot"]
    D5["cmd"]
    D6["colors"]
    D7["cost"]
    D8["docs"]
    D9["dryrun"]
    D10["exec"]
    D11["function"]
    D12["hooks"]
    D13["infra"]
    D14["internal"]
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

**Directories:** `.github`, `_examples`, `archive`, `assets`, `boot`, `cmd`, `colors`, `cost`, `docs`, `dryrun`, `exec`, `function`, `hooks`, `infra`, `internal`, `logs`, `metrics`, `mock`, `plugins`, `project`, `service`, `shim`, `upgrade`, `utils`, `vpc`

**Notable files:** `.gitignore`, `.goreleaser.yml`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `go.mod`, `go.sum`, `History.md`, `install.sh`, `LICENSE`, `Makefile`, `Readme.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Cmd["cmd / main"] --> App["apex"]
  App --> Pkgs["Internal packages"]
  Pkgs --> Ext["External services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Go | 66 files |
| JavaScript | 33 files |
| Python | 3 files |
| Gradle | 2 files |
| Java | 2 files |
| Ruby | 2 files |
| Groovy | 1 files |
| XML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Go |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/apex](https://github.com/WycliffeAssociates/apex)
- Branch analyzed: `master`

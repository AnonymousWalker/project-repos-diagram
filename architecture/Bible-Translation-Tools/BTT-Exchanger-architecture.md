# BTT-Exchanger architecture

[Bible-Translation-Tools/BTT-Exchanger](https://github.com/Bible-Translation-Tools/BTT-Exchanger) — Release repo for Translation Exchange project.

BTT Exchanger is a platform for backup, checking, collating, and exporting oral bible translation

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTT-Exchanger"]
    M0["admin-client"]
    M1["android-client"]
    M2["ap"]
    M3["install"]
    M4["web"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: JavaScript"]
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
  Root["BTT-Exchanger<br/>Release repo for Translation Exchange project"]

  subgraph structure["Top-level layout"]
    D0["admin-client"]
    D1["android-client"]
    D2["ap"]
    D3["install"]
    D4["web"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `admin-client`, `android-client`, `ap`, `install`, `web`

**Notable files:** `.gitignore`, `build.sh`, `crowdin.yml`, `LICENSE`, `README.md`, `release.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["BTT-Exchanger"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 351 files |
| Python | 99 files |
| XML | 33 files |
| Shell | 25 files |
| CSS | 18 files |
| YAML | 13 files |
| Java | 9 files |
| Gradle | 6 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | JavaScript |
| **Default branch** | `dev` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BTT-Exchanger](https://github.com/Bible-Translation-Tools/BTT-Exchanger)
- Branch analyzed: `dev`

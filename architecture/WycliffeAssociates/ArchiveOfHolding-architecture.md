# ArchiveOfHolding architecture

[WycliffeAssociates/ArchiveOfHolding](https://github.com/WycliffeAssociates/ArchiveOfHolding) — An uncompressed archive format with a JSON Table of Contents Header.

An uncompressed archive format with a JSON Table of Contents Header

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ArchiveOfHolding"]
    M0["aoh"]
    M1["cli"]
    M2["gradle"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Java"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ArchiveOfHolding<br/>An uncompressed archive format with a JSON Table of Contents Header"]

  subgraph structure["Top-level layout"]
    D0["aoh"]
    D1["cli"]
    D2["gradle"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `aoh`, `cli`, `gradle`

**Notable files:** `.gitattributes`, `.gitignore`, `build.gradle`, `gradlew`, `gradlew.bat`, `LICENSE`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["ArchiveOfHolding"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Java | 6 files |
| Gradle | 4 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ArchiveOfHolding](https://github.com/WycliffeAssociates/ArchiveOfHolding)
- Branch analyzed: `master`

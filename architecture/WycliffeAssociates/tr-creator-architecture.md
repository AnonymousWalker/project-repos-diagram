# tr-creator architecture

[WycliffeAssociates/tr-creator](https://github.com/WycliffeAssociates/tr-creator) — Create TR files.

Create TR files from BTT Recorder projects

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tr-creator"]
    M0["gradle"]
    M1["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tr-creator<br/>Create TR files"]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `gradle`, `src`

**Notable files:** `.gitignore`, `build.gradle`, `crowdin.yml`, `gradle.properties`, `gradlew`, `gradlew.bat`, `launcher.ico`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["tr-creator"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 9 files |
| Gradle | 2 files |
| YAML | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tr-creator](https://github.com/WycliffeAssociates/tr-creator)
- Branch analyzed: `master`

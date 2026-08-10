# BTTConverter architecture

[Bible-Translation-Tools/BTTConverter](https://github.com/Bible-Translation-Tools/BTTConverter) — translationRecorder Converter.

Converter library for BTT Recorder

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTTConverter"]
    M0["gradle"]
    M1["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Java"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["BTTConverter<br/>translationRecorder Converter"]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `gradle`, `src`

**Notable files:** `.gitignore`, `build.gradle`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["BTTConverter"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Java | 21 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BTTConverter](https://github.com/Bible-Translation-Tools/BTTConverter)
- Branch analyzed: `master`

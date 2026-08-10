# tr-wav architecture

[WycliffeAssociates/tr-wav](https://github.com/WycliffeAssociates/tr-wav) — A Kotlin library for working with tR WAV audio file metadata..

A Kotlin library for working with tR WAV audio file metadata. Ported from the [BTT Recorder Android app](https://github.com/Bible-Translation-Tools/BTT-Recorder/tree/dev/translationRecorder/app/src/main/java/org/wycliffeassociates/translationrecorder/wav).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tr-wav"]
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
  Root["tr-wav<br/>A Kotlin library for working with tR WAV audio file metadata."]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `gradle`, `src`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["tr-wav"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 17 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tr-wav](https://github.com/WycliffeAssociates/tr-wav)
- Branch analyzed: `master`

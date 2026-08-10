# tr-chunk-browser architecture

[WycliffeAssociates/tr-chunk-browser](https://github.com/WycliffeAssociates/tr-chunk-browser) — A Kotlin, TornadoFX app for working with tR audio files..

This application can import and identify verses within tR audio file chunks. After importing tR audio files containing verses, you may selectively split verses into separate files and merge verses into a chunk audio file, all while maintaining the tR metadata.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tr-chunk-browser"]
    M0["cli"]
    M1["common"]
    M2["gradle"]
    M3["jvm"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tr-chunk-browser<br/>A Kotlin, TornadoFX app for working with tR audio files."]

  subgraph structure["Top-level layout"]
    D0["cli"]
    D1["common"]
    D2["gradle"]
    D3["jvm"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `cli`, `common`, `gradle`, `jvm`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `crowdin.yml`, `dependencies.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `launcher.ico`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["tr-chunk-browser"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 33 files |
| Gradle | 6 files |
| YAML | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tr-chunk-browser](https://github.com/WycliffeAssociates/tr-chunk-browser)
- Branch analyzed: `master`

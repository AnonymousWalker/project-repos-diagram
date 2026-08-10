# AudioCompressorAndroid architecture

[Bible-Translation-Tools/AudioCompressorAndroid](https://github.com/Bible-Translation-Tools/AudioCompressorAndroid) — Converts a zip of mp3 to wav and vice versa.

Converts a zip of mp3 to wav and vice versa

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["AudioCompressorAndroid"]
    M0[".idea"]
    M1["app"]
    M2["gradle"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: XML"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["AudioCompressorAndroid<br/>Converts a zip of mp3 to wav and vice versa"]

  subgraph structure["Top-level layout"]
    D0[".idea"]
    D1["app"]
    D2["gradle"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.idea`, `app`, `gradle`

**Notable files:** `.gitattributes`, `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["AudioCompressorAndroid"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 11 files |
| Kotlin | 7 files |
| Gradle | 3 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/AudioCompressorAndroid](https://github.com/Bible-Translation-Tools/AudioCompressorAndroid)
- Branch analyzed: `master`

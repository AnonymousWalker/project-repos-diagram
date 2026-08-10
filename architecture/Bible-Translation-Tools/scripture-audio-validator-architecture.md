# scripture-audio-validator architecture

[Bible-Translation-Tools/scripture-audio-validator](https://github.com/Bible-Translation-Tools/scripture-audio-validator) — _no GitHub description_.

scripture-audio-validator is a public repository under Bible-Translation-Tools.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["scripture-audio-validator"]
    M0["common"]
    M1["gradle"]
    M2["web"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-audio-validator<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["common"]
    D1["gradle"]
    D2["web"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `common`, `gradle`, `web`

**Notable files:** `.gitignore`, `build.gradle`, `dependencies.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["scripture-audio-validator"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 64 files |
| Gradle | 5 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `aw-dev` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/scripture-audio-validator](https://github.com/Bible-Translation-Tools/scripture-audio-validator)
- Branch analyzed: `aw-dev`

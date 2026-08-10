# Orature-Plugin architecture

[Bible-Translation-Tools/Orature-Plugin](https://github.com/Bible-Translation-Tools/Orature-Plugin) — A base repo to create an audio plugin for Orature.

A base repo to create an audio plugin for Orature

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Orature-Plugin"]
    M0["gradle"]
    M1["screenshots"]
    M2["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Gradle"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Orature-Plugin<br/>A base repo to create an audio plugin for Orature"]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["screenshots"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `gradle`, `screenshots`, `src`

**Notable files:** `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["Orature-Plugin"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Gradle | 2 files |
| Batch | 1 files |
| Java | 1 files |
| Kotlin | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Orature-Plugin](https://github.com/Bible-Translation-Tools/Orature-Plugin)
- Branch analyzed: `main`

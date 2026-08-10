# Reaper-Orature-Plugin architecture

[Bible-Translation-Tools/Reaper-Orature-Plugin](https://github.com/Bible-Translation-Tools/Reaper-Orature-Plugin) — _no GitHub description_.

Reaper audio plugin for Orature

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Reaper-Orature-Plugin"]
    M0["gradle"]
    M1["screenshots"]
    M2["src"]
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
  Root["Reaper-Orature-Plugin<br/>No description on GitHub"]

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

**Notable files:** `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `RipperOraturePlugin.lua`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["Reaper-Orature-Plugin"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 7 files |
| Gradle | 2 files |
| Batch | 1 files |
| Java | 1 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Reaper-Orature-Plugin](https://github.com/Bible-Translation-Tools/Reaper-Orature-Plugin)
- Branch analyzed: `master`

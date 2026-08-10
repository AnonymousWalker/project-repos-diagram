# Spotlight architecture

[Bible-Translation-Tools/Spotlight](https://github.com/Bible-Translation-Tools/Spotlight) — _no GitHub description_.

This is a Kotlin Multiplatform project targeting Android, Web, Desktop.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Spotlight"]
    M0[".github"]
    M1["androidApp"]
    M2["api"]
    M3["desktopApp"]
    M4["gradle"]
    M5["shared"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Spotlight<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["androidApp"]
    D2["api"]
    D3["desktopApp"]
    D4["gradle"]
    D5["shared"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.github`, `androidApp`, `api`, `desktopApp`, `gradle`, `shared`

**Notable files:** `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["Spotlight"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 186 files |
| XML | 25 files |
| SQL | 17 files |
| TypeScript | 10 files |
| HTML | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Spotlight](https://github.com/Bible-Translation-Tools/Spotlight)
- Branch analyzed: `master`

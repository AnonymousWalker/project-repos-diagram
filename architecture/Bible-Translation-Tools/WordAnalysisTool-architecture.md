# WordAnalysisTool architecture

[Bible-Translation-Tools/WordAnalysisTool](https://github.com/Bible-Translation-Tools/WordAnalysisTool) — _no GitHub description_.

This is WordAnalysisTool targeting Android, Web, Desktop.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["WordAnalysisTool"]
    M0["androidApp"]
    M1["api"]
    M2["gradle"]
    M3["kotlin-js-store"]
    M4["shared"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["WordAnalysisTool<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["androidApp"]
    D1["api"]
    D2["gradle"]
    D3["kotlin-js-store"]
    D4["shared"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `androidApp`, `api`, `gradle`, `kotlin-js-store`, `shared`

**Notable files:** `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["WordAnalysisTool"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 117 files |
| XML | 11 files |
| TypeScript | 10 files |
| SQL | 5 files |
| Batch | 1 files |
| HTML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/WordAnalysisTool](https://github.com/Bible-Translation-Tools/WordAnalysisTool)
- Branch analyzed: `master`

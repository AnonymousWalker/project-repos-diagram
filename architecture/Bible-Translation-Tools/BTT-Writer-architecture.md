# BTT-Writer architecture

[Bible-Translation-Tools/BTT-Writer](https://github.com/Bible-Translation-Tools/BTT-Writer) — BTT-Writer Multiplatform.

BTT-Writer Multiplatform

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTT-Writer"]
    M0[".github"]
    M1[".maestro"]
    M2["androidApp"]
    M3["desktopApp"]
    M4["docs"]
    M5["gradle"]
    M6["shared"]
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
  Users --> M6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["BTT-Writer<br/>BTT-Writer Multiplatform"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".maestro"]
    D2["androidApp"]
    D3["desktopApp"]
    D4["docs"]
    D5["gradle"]
    D6["shared"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
```

**Directories:** `.github`, `.maestro`, `androidApp`, `desktopApp`, `docs`, `gradle`, `shared`

**Notable files:** `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["BTT-Writer"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 427 files |
| XML | 12 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `default` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BTT-Writer](https://github.com/Bible-Translation-Tools/BTT-Writer)
- Branch analyzed: `default`

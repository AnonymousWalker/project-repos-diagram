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
    M1["androidApp"]
    M2["composeApp"]
    M3["gradle"]
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
  Root["BTT-Writer<br/>BTT-Writer Multiplatform"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["androidApp"]
    D2["composeApp"]
    D3["gradle"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `androidApp`, `composeApp`, `gradle`

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
| Kotlin | 349 files |
| XML | 11 files |
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

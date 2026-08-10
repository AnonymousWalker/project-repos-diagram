# maui architecture

[Bible-Translation-Tools/maui](https://github.com/Bible-Translation-Tools/maui) — _no GitHub description_.

maui is a public repository under Bible-Translation-Tools.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["maui"]
    M0["common"]
    M1["config"]
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
  Root["maui<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["common"]
    D1["config"]
    D2["gradle"]
    D3["jvm"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `common`, `config`, `gradle`, `jvm`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `dependencies.gradle`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`, `sonar-project.properties`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["maui"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 83 files |
| Gradle | 5 files |
| CSS | 5 files |
| YAML | 1 files |
| Batch | 1 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `dev` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/maui](https://github.com/Bible-Translation-Tools/maui)
- Branch analyzed: `dev`

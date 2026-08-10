# BTTConverterDesktop architecture

[Bible-Translation-Tools/BTTConverterDesktop](https://github.com/Bible-Translation-Tools/BTTConverterDesktop) — BTTConverter for Desktop.

BTTConverter for Desktop

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTTConverterDesktop"]
    M0["converter"]
    M1["gradle"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["BTTConverterDesktop<br/>BTTConverter for Desktop"]

  subgraph structure["Top-level layout"]
    D0["converter"]
    D1["gradle"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `converter`, `gradle`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `crowdin.yml`, `gradlew`, `gradlew.bat`, `jar2appvars.env`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["BTTConverterDesktop"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 26 files |
| CSS | 8 files |
| Gradle | 3 files |
| YAML | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BTTConverterDesktop](https://github.com/Bible-Translation-Tools/BTTConverterDesktop)
- Branch analyzed: `master`

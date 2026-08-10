# kotlin-tstudio2rc architecture

[WycliffeAssociates/kotlin-tstudio2rc](https://github.com/WycliffeAssociates/kotlin-tstudio2rc) — _no GitHub description_.

kotlin-tstudio2rc is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["kotlin-tstudio2rc"]
    M0["gradle"]
    M1["src"]
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
  Root["kotlin-tstudio2rc<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `gradle`, `src`

**Notable files:** `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["kotlin-tstudio2rc"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 15 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/kotlin-tstudio2rc](https://github.com/WycliffeAssociates/kotlin-tstudio2rc)
- Branch analyzed: `main`

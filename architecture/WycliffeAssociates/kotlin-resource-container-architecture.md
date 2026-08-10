# kotlin-resource-container architecture

[WycliffeAssociates/kotlin-resource-container](https://github.com/WycliffeAssociates/kotlin-resource-container) — Kotlin implementation of the Door43 Resource Container.

This library implements the Door43 Content Services resource container specification for the kotlin language. This library provides kotlin type safe builders for constructing a resource container.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["kotlin-resource-container"]
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
  Root["kotlin-resource-container<br/>Kotlin implementation of the Door43 Resource Container"]

  subgraph structure["Top-level layout"]
    D0["gradle"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `gradle`, `src`

**Notable files:** `.gitattributes`, `.gitignore`, `.travis.yml`, `build.gradle`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["kotlin-resource-container"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 27 files |
| YAML | 13 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `dev` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/kotlin-resource-container](https://github.com/WycliffeAssociates/kotlin-resource-container)
- Branch analyzed: `dev`

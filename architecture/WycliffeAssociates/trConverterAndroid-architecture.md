# trConverterAndroid architecture

[WycliffeAssociates/trConverterAndroid](https://github.com/WycliffeAssociates/trConverterAndroid) — _no GitHub description_.

trConverterAndroid is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["trConverterAndroid"]
    M0["app"]
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
  Root["trConverterAndroid<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["app"]
    D1["gradle"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `app`, `gradle`

**Notable files:** `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["trConverterAndroid"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 24 files |
| XML | 18 files |
| Gradle | 3 files |
| Java | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/trConverterAndroid](https://github.com/WycliffeAssociates/trConverterAndroid)
- Branch analyzed: `master`

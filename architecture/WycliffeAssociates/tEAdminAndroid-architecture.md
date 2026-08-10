# tEAdminAndroid architecture

[WycliffeAssociates/tEAdminAndroid](https://github.com/WycliffeAssociates/tEAdminAndroid) — Android app for Translation Exchange Admin.

moved to https://github.com/Bible-Translation-Tools/BTT-Exchanger

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tEAdminAndroid"]
    M0["app"]
    M1["gradle"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: XML"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tEAdminAndroid<br/>Android app for Translation Exchange Admin"]

  subgraph structure["Top-level layout"]
    D0["app"]
    D1["gradle"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `app`, `gradle`

**Notable files:** `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["tEAdminAndroid"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 16 files |
| Java | 5 files |
| Gradle | 3 files |
| JavaScript | 3 files |
| HTML | 1 files |
| CSS | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tEAdminAndroid](https://github.com/WycliffeAssociates/tEAdminAndroid)
- Branch analyzed: `master`

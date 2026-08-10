# BTTConverterAndroid architecture

[Bible-Translation-Tools/BTTConverterAndroid](https://github.com/Bible-Translation-Tools/BTTConverterAndroid) — _no GitHub description_.

BTTConverterAndroid is a public repository under Bible-Translation-Tools.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTTConverterAndroid"]
    M0["app"]
    M1["gradle"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Java"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["BTTConverterAndroid<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["app"]
    D1["gradle"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `app`, `gradle`

**Notable files:** `.gitignore`, `build.gradle`, `crowdin.yml`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["BTTConverterAndroid"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Java | 17 files |
| XML | 14 files |
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

- Source: [Bible-Translation-Tools/BTTConverterAndroid](https://github.com/Bible-Translation-Tools/BTTConverterAndroid)
- Branch analyzed: `master`

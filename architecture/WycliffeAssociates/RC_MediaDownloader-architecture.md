# RC_MediaDownloader architecture

[WycliffeAssociates/RC_MediaDownloader](https://github.com/WycliffeAssociates/RC_MediaDownloader) — _no GitHub description_.

This tool supports downloading media content to the given resource container and update the urls with respect to the resource container itself.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["RC_MediaDownloader"]
    M0["cliapp"]
    M1["config"]
    M2["gradle"]
    M3["lib"]
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
  Root["RC_MediaDownloader<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["cliapp"]
    D1["config"]
    D2["gradle"]
    D3["lib"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `cliapp`, `config`, `gradle`, `lib`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `dependencies.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`, `sonar-project.properties`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["RC_MediaDownloader"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 12 files |
| Gradle | 5 files |
| YAML | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/RC_MediaDownloader](https://github.com/WycliffeAssociates/RC_MediaDownloader)
- Branch analyzed: `master`

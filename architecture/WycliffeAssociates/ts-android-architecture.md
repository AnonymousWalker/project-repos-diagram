# ts-android architecture

[WycliffeAssociates/ts-android](https://github.com/WycliffeAssociates/ts-android) — Bible Translation Tools Writer Application.

Repo is archived. New repo is here: https://github.com/Bible-Translation-Tools/BTT-Writer-Android

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ts-android"]
    M0[".github"]
    M1["app"]
    M2["gradle"]
    M3["html-textview"]
    M4["seekbarhint"]
    M5["tools"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: XML"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ts-android<br/>Bible Translation Tools Writer Application"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["app"]
    D2["gradle"]
    D3["html-textview"]
    D4["seekbarhint"]
    D5["tools"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.github`, `app`, `gradle`, `html-textview`, `seekbarhint`, `tools`

**Notable files:** `.gitignore`, `.travis.yml`, `build.gradle`, `COPYING`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `readme-noto-font.txt`, `README.md`, `secrets.tar.enc`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["ts-android"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 303 files |
| Java | 270 files |
| Gradle | 5 files |
| SQL | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ts-android](https://github.com/WycliffeAssociates/ts-android)
- Branch analyzed: `master`

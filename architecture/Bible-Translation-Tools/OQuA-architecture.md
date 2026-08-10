# OQuA architecture

[Bible-Translation-Tools/OQuA](https://github.com/Bible-Translation-Tools/OQuA) — _no GitHub description_.

Orature is an application for oral drafting, narration, and translation of the Bible, books (such as [Open Bible Stories](https://www.unfoldingword.org/open-bible-stories)), and translation helps/resources (such as notes and checking questions). Additionally, Orature can connect with third party applications for more expansive recording and editing options. More information can be found [here.](https://bibletranslationtools.org/tool/orature/), as well as in the [wiki.](https://github.com/Bible-Translation-Tools/Orature/wiki)

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["OQuA"]
    M0[".github"]
    M1["assets"]
    M2["common"]
    M3["config"]
    M4["gradle"]
    M5["jvm"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
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
  Root["OQuA<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["assets"]
    D2["common"]
    D3["config"]
    D4["gradle"]
    D5["jvm"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.github`, `assets`, `common`, `config`, `gradle`, `jvm`

**Notable files:** `.gitattributes`, `.gitignore`, `.sonarcloud.properties`, `build.gradle`, `COPYING`, `crowdin.yml`, `dependencies.gradle`, `dev-build.sh`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`, `signing.p12.gpg`, `sonar-project.properties`, `VERSION`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["OQuA"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 558 files |
| CSS | 54 files |
| Gradle | 15 files |
| YAML | 13 files |
| SQL | 2 files |
| Shell | 1 files |
| Batch | 1 files |
| Java | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `dev` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/OQuA](https://github.com/Bible-Translation-Tools/OQuA)
- Branch analyzed: `dev`

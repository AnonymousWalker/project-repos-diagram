# USFMToolsJava architecture

[WycliffeAssociates/USFMToolsJava](https://github.com/WycliffeAssociates/USFMToolsJava) — A Java port of USFMToolsSharp.

A Java port of USFMToolsSharp

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsJava"]
    M0[".github"]
    M1["gradle"]
    M2["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Java"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["USFMToolsJava<br/>A Java port of USFMToolsSharp"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["gradle"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `gradle`, `src`

**Notable files:** `.gitattributes`, `.gitignore`, `.travis.yml`, `build.gradle`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["USFMToolsJava"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Java | 163 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsJava](https://github.com/WycliffeAssociates/USFMToolsJava)
- Branch analyzed: `master`

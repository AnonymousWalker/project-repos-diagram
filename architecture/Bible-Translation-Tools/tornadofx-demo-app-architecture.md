# tornadofx-demo-app architecture

[Bible-Translation-Tools/tornadofx-demo-app](https://github.com/Bible-Translation-Tools/tornadofx-demo-app) — A demo application using torandofx.

A simple, preconfigured gradle project to use as a starting point for new javafx projects

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tornadofx-demo-app"]
    M0[".github"]
    M1["gradle"]
    M2["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Gradle / JVM"]
    Lang["Primary language: Kotlin"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tornadofx-demo-app<br/>A demo application using torandofx"]

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

**Notable files:** `.gitattributes`, `.gitignore`, `build.gradle`, `dependencies.gradle`, `gradlew`, `gradlew.bat`, `README.md`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["tornadofx-demo-app"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 24 files |
| Gradle | 3 files |
| CSS | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/tornadofx-demo-app](https://github.com/Bible-Translation-Tools/tornadofx-demo-app)
- Branch analyzed: `main`

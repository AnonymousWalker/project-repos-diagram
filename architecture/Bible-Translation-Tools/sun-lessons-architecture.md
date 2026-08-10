# sun-lessons architecture

[Bible-Translation-Tools/sun-lessons](https://github.com/Bible-Translation-Tools/sun-lessons) — _no GitHub description_.

It's an app learning SUN by flashcards.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["sun-lessons"]
    M0[".github"]
    M1["app"]
    M2["gradle"]
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
  Root["sun-lessons<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["app"]
    D2["gradle"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `app`, `gradle`

**Notable files:** `.deepsource.toml`, `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["sun-lessons"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 124 files |
| XML | 32 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/sun-lessons](https://github.com/Bible-Translation-Tools/sun-lessons)
- Branch analyzed: `main`

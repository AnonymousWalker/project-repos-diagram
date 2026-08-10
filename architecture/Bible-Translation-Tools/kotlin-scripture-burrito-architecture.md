# kotlin-scripture-burrito architecture

[Bible-Translation-Tools/kotlin-scripture-burrito](https://github.com/Bible-Translation-Tools/kotlin-scripture-burrito) — A Kotlin library for Scripture Burrito.

A Kotlin library for Scripture Burrito

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["kotlin-scripture-burrito"]
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
  Root["kotlin-scripture-burrito<br/>A Kotlin library for Scripture Burrito"]

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

**Notable files:** `.gitignore`, `build.gradle`, `gradlew`, `gradlew.bat`, `LICENSE`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["kotlin-scripture-burrito"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 77 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `default` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/kotlin-scripture-burrito](https://github.com/Bible-Translation-Tools/kotlin-scripture-burrito)
- Branch analyzed: `default`

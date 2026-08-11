# Audio-Bible-Software architecture

[Bible-Translation-Tools/Audio-Bible-Software](https://github.com/Bible-Translation-Tools/Audio-Bible-Software) — A monorepo of Audio Bible Applications, namely BTT-Recorder and Orature.

This is a Kotlin Multiplatform project targeting Android, Desktop.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Audio-Bible-Software"]
    M0[".agent"]
    M1[".github"]
    M2["app-orature"]
    M3["app-recorder"]
    M4["gradle"]
    M5["proguard"]
    M6["shared"]
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
  Users --> M6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Audio-Bible-Software<br/>A monorepo of Audio Bible Applications, namely BTT-Recorder and Orature"]

  subgraph structure["Top-level layout"]
    D0[".agent"]
    D1[".github"]
    D2["app-orature"]
    D3["app-recorder"]
    D4["gradle"]
    D5["proguard"]
    D6["shared"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
```

**Directories:** `.agent`, `.github`, `app-orature`, `app-recorder`, `gradle`, `proguard`, `shared`

**Notable files:** `.gitattributes`, `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["Audio-Bible-Software"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 579 files |
| XML | 22 files |
| Gradle | 3 files |
| SQL | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/Audio-Bible-Software](https://github.com/Bible-Translation-Tools/Audio-Bible-Software)
- Branch analyzed: `main`

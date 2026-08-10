# AudioScripts architecture

[Bible-Translation-Tools/AudioScripts](https://github.com/Bible-Translation-Tools/AudioScripts) — Various scripts to examine audio and cue content.

Various scripts to examine audio and cue content

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["AudioScripts"]
    M0[".idea"]
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
  Root["AudioScripts<br/>Various scripts to examine audio and cue content"]

  subgraph structure["Top-level layout"]
    D0[".idea"]
    D1["gradle"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.idea`, `gradle`, `src`

**Notable files:** `.gitattributes`, `.gitignore`, `build.gradle`, `gradle.properties`, `gradlew`, `gradlew.bat`, `LICENSE`, `results.json`, `settings.gradle`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["AudioScripts"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 9 files |
| Gradle | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/AudioScripts](https://github.com/Bible-Translation-Tools/AudioScripts)
- Branch analyzed: `main`

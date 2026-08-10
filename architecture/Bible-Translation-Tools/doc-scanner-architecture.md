# doc-scanner architecture

[Bible-Translation-Tools/doc-scanner](https://github.com/Bible-Translation-Tools/doc-scanner) — Simple Doc Scanner with Google's ML kit object detection library.

DocScanner is a native **Kotlin Multiplatform (KMP)** application targeting Android and iOS. It is designed to capture physical handwritten documents, manage translation projects, render pages to images, and send them to a Cloudflare Workers backend for **Handwritten Text Recognition (HTR)** transcription using state-of-the-art AI models.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["doc-scanner"]
    M0[".github"]
    M1["androidApp"]
    M2["gradle"]
    M3["iosApp"]
    M4["shared"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["doc-scanner<br/>Simple Doc Scanner with Google's ML kit object detection library"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["androidApp"]
    D2["gradle"]
    D3["iosApp"]
    D4["shared"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.github`, `androidApp`, `gradle`, `iosApp`, `shared`

**Notable files:** `.gitignore`, `build.gradle.kts`, `gradle.properties`, `gradlew`, `gradlew.bat`, `play_store_feature_graphic.png`, `play_store_icon.png`, `README.md`, `settings.gradle.kts`


## Runtime / integration sketch

```mermaid
flowchart LR
  App["doc-scanner"] --> Domain["Domain / business logic"]
  Domain --> Data["Persistence / files / APIs"]
  App --> UI["UI or CLI entrypoints"]
  Data --> Ext["External libs / services"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Kotlin | 70 files |
| XML | 11 files |
| Swift | 2 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Gradle / JVM |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/doc-scanner](https://github.com/Bible-Translation-Tools/doc-scanner)
- Branch analyzed: `main`

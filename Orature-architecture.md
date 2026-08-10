# Orature architecture

[Orature](https://github.com/Bible-Translation-Tools/Orature) is a desktop application for oral Bible drafting, narration, and translation. The Gradle project is named **otter** (Oral Translation Tools and Resources). The codebase is split into **Common** (shared logic for desktop and future Android) and **JVM** (JavaFX desktop implementation).

## System context

```mermaid
flowchart TB
  subgraph users["Users"]
    Translator["Translators / narrators"]
  end

  subgraph orature["Orature desktop (JavaFX)"]
    WorkbookApp["workbookapp — main Orature UI"]
    RecorderApp["recorderapp — standalone recorder"]
    MarkerApp["markerapp — verse markers in audio"]
  end

  subgraph content["Scripture content"]
    RC["Door43 Resource Container (.zip)"]
    Burrito["Scripture Burrito metadata"]
    USFM["USFM scripture"]
    MD["Markdown (OBS, helps)"]
    SrcAudio["Source audio WAV/MP3 + media manifest"]
  end

  subgraph external["External services & tools"]
    LangAPI["Language catalog (HTTP / Retrofit)"]
    AudioPlugins["Third-party recorder / editor plugins"]
    Updater["install4j auto-updater"]
  end

  Translator --> WorkbookApp
  Translator --> RecorderApp
  Translator --> MarkerApp

  WorkbookApp --> RC
  RC --> USFM
  RC --> MD
  RC --> SrcAudio
  RC --> Burrito

  WorkbookApp --> LangAPI
  WorkbookApp --> AudioPlugins
  WorkbookApp --> Updater
```

## Gradle modules & layering

```mermaid
flowchart TB
  subgraph jvm_apps["JVM applications"]
    WB["jvm:workbookapp<br/>OtterApp entry"]
    REC["jvm:recorderapp"]
    MRK["jvm:markerapp"]
  end

  subgraph jvm_platform["JVM platform"]
    DEV["jvm:device<br/>microphone / playback"]
    CTL["jvm:controls<br/>shared JavaFX controls"]
    UTL["jvm:utils"]
    PLG["jvm:workbookplugin<br/>plugin host UI"]
  end

  subgraph common_layer["Common (cross-platform intent)"]
    COM["common<br/>domain + repository interfaces"]
    AUD["common:audio<br/>WAV/MP3, cues, DSP"]
  end

  subgraph assets["Resources"]
    AST["assets<br/>images, strings, themes"]
  end

  subgraph persistence["Local persistence"]
    SQL["SQLite"]
    JOOQ["JOOQ-generated DAOs"]
  end

  subgraph libs["Key libraries"]
    RC_LIB["kotlin-resource-container"]
    BUR["kotlin-scripture-burrito"]
    USFM_LIB["usfmtools"]
    RX["RxJava2 / RxKotlinFX"]
    DAG["Dagger DI"]
    TFx["TornadoFX + JavaFX 21"]
  end

  WB --> COM
  WB --> AUD
  WB --> DEV
  WB --> CTL
  WB --> UTL
  WB --> PLG
  WB --> AST
  REC --> COM
  REC --> AUD
  REC --> DEV
  REC --> CTL
  REC --> PLG
  MRK --> COM
  MRK --> AUD
  MRK --> DEV
  MRK --> CTL
  MRK --> UTL
  MRK --> PLG

  COM --> AUD
  COM --> RC_LIB
  COM --> BUR
  COM --> USFM_LIB

  WB --> SQL
  SQL --> JOOQ

  WB --> DAG
  WB --> TFx
  WB --> RX
```

## Runtime flow inside `workbookapp`

```mermaid
flowchart LR
  subgraph ui["Presentation"]
    Root["RootView / screens"]
    VM["ViewModels"]
    Nar["Narration UI<br/>waveform, markers"]
    Trans["Translation / chunking UI"]
  end

  subgraph di["Composition"]
    Graph["DaggerAppDependencyGraph"]
  end

  subgraph domain["Domain (common)"]
    Proj["project / collections"]
    Narr["narration use cases"]
    Transl["translation & chunk audio"]
    RCImp["resourcecontainer import/export"]
    Plugins["audio plugin registry"]
  end

  subgraph data["Data"]
    RepoIf["I*Repository interfaces"]
    RepoJvm["JVM repository impls"]
    DB["AppDatabase (SQLite)"]
    Files["DirectoryProvider<br/>project & take files"]
  end

  subgraph io["I/O & media"]
    Zip["RC zip read/write"]
    Parse["USFM / Markdown / Burrito parsers"]
    Play["common:audio playback"]
    Rec["jvm:device recording"]
  end

  Root --> VM
  VM --> Nar
  VM --> Trans
  VM --> Graph
  Graph --> domain
  Graph --> RepoJvm
  domain --> RepoIf
  RepoJvm -.implements.-> RepoIf
  RepoJvm --> DB
  domain --> Files
  domain --> Zip
  Zip --> Parse
  Nar --> Play
  Nar --> Rec
  Plugins --> Rec
```

## Design notes

| Topic | Approach |
|--------|----------|
| **Platforms** | Interfaces and domain logic live in `common`; JVM-specific code (JavaFX, SQLite repos, filesystem) lives under `jvm`. |
| **UI stack** | JavaFX 21, TornadoFX, MaterialFX / JFoenix controls, RxJava for async streams. |
| **Projects** | Imported/exported as Resource Containers; supports Burrito metadata, USFM, Markdown, and container-local source audio. |
| **State** | Workbooks, takes, resources, languages, and preferences persisted in SQLite via JOOQ. |
| **Extensibility** | YAML-defined **audio plugins** launch external recorders/editors; `workbookplugin` shares plugin UI across apps. |
| **Build / ship** | Gradle wrapper (`./gradlew run`); installers via install4j (Windows, Linux, macOS). |

## Related repositories

- Source: [Bible-Translation-Tools/Orature](https://github.com/Bible-Translation-Tools/Orature)
- Product info: [bibletranslationtools.org — Orature](https://bibletranslationtools.org/tool/orature/)
- Resource Container spec: [Door43 Resource Container](https://resource-container.readthedocs.io/)

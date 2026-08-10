# Fetcher architecture

[Fetcher](https://github.com/Bible-Translation-Tools/Fetcher) is an app/library for downloading scripture **source audio** for translation. It is a Docker-composed system: a **Kotlin/Ktor web UI** that browses and packages audio into Resource Containers, a **Python pipeline** that processes uploaded WAV into MP3 / TR / book artifacts, an **FTP** intake, and a **CDN-style file server**.

Default branch in this org listing: `audio.bibleineverylanguage.org`.

## System context

```mermaid
flowchart TB
  subgraph users["Users"]
    Translator["Translators / content consumers"]
    Uploader["Audio publishers / uploaders"]
  end

  subgraph fetcher["Fetcher stack (Docker Compose)"]
    Web["fetcher-web — Ktor UI + RC packaging"]
    Pipeline["fetcher-pipeline — audio workers"]
    FTP["FTP server — intake volume"]
    FileSrv["fileserver — HTTP CDN for content / RC"]
  end

  subgraph content["Content artifacts"]
    WAV["Chapter / verse WAV"]
    MP3["MP3 hi / low"]
    TR["BTTR (.tr) packages"]
    BookAudio["Book-level WAV / MP3"]
    RC["Door43 Resource Container (.zip)"]
  end

  subgraph external["External sources"]
    BielGQL["BIEL GraphQL — primary git repos"]
    UWLang["UnfoldingWord language names"]
    GLRepos["Gateway-language Orature git repos"]
    AzureSB["Azure Service Bus — pipeline events"]
  end

  Translator --> Web
  Uploader --> FTP
  FTP --> Pipeline
  Pipeline --> WAV
  Pipeline --> MP3
  Pipeline --> TR
  Pipeline --> BookAudio
  Web --> FileSrv
  Web --> RC
  FileSrv --> WAV
  FileSrv --> MP3
  FileSrv --> TR
  FileSrv --> BookAudio
  FileSrv --> RC

  Web --> BielGQL
  Web --> UWLang
  Pipeline --> GLRepos
  Pipeline --> AzureSB
```

## Deployed services & volumes

```mermaid
flowchart LR
  subgraph compose["dockerstack"]
    FA["fetcher-app<br/>port 8080"]
    PL["pipeline"]
    FT["ftp<br/>ports 20/21"]
    FS["fileserver<br/>port 8081"]
  end

  subgraph vols["Shared volumes"]
    Content["fetcher-content<br/>FTP root / CDN content"]
    RCTemp["fetcher-rc<br/>RC_TEMP_DIR"]
    Repos["fetcher-repos<br/>ORATURE_REPO_DIR"]
  end

  FT --> Content
  PL --> Content
  PL --> RCTemp
  PL --> Repos
  FA --> Content
  FA --> RCTemp
  FA --> Repos
  FS --> Content
  FS --> RCTemp
```

## `fetcher-web` layering

```mermaid
flowchart TB
  subgraph presentation["Presentation"]
    Main["Main.kt — Netty :8080"]
    Controllers["Controllers<br/>home · language · product · book · chapter"]
    Thymeleaf["Thymeleaf HTML templates"]
  end

  subgraph usecases["Use cases"]
    FetchVD["Fetch*ViewData"]
    Deliverable["DeliverableBuilder"]
    Ext["ProductFileExtension<br/>mp3 · wav · tr · orature/zip"]
  end

  subgraph di["Composition"]
    Koin["Koin appDependencyModule"]
  end

  subgraph repos["Repositories (interfaces → impl)"]
    LangRepo["LanguageRepository / Catalog"]
    BookRepo["BookRepository / Catalog"]
    ChapterCat["ChapterCatalog"]
    ProductCat["ProductCatalog"]
    Storage["StorageAccess"]
    RCRepo["ResourceContainerRepository"]
    ReqRC["RequestResourceContainer<br/>+ RCMediaDownloader"]
    SourceText["SourceTextAccessor<br/>Apollo GraphQL cache"]
  end

  subgraph libs["Key libraries"]
    Ktor["Ktor Netty"]
    RCLib["kotlin-resource-container"]
    RCMedia["rcmediadownloader"]
    Apollo["Apollo GraphQL"]
    Retrofit["Retrofit / HTTP"]
  end

  Main --> Controllers
  Controllers --> Thymeleaf
  Controllers --> FetchVD
  Controllers --> Deliverable
  Controllers --> Koin
  FetchVD --> Ext
  Deliverable --> LangRepo
  Deliverable --> BookRepo
  Deliverable --> ProductCat
  FetchVD --> Storage
  FetchVD --> ReqRC
  ReqRC --> RCRepo
  ReqRC --> RCLib
  ReqRC --> RCMedia
  SourceText --> Apollo
  LangRepo --> Retrofit
  Controllers --> Ktor
```

## Browse & download flow

```mermaid
flowchart LR
  Home["/"] --> Lang["/language"]
  Lang --> Product["/…/product"]
  Product --> Book["/…/book"]
  Book --> Chapter["/…/chapter"]

  Chapter --> CDN["Link to CDN file<br/>WAV / MP3 / TR"]
  Product --> Zip["Build Orature RC zip<br/>RequestResourceContainer"]
  Zip --> Media["Attach media via<br/>RCMediaDownloader"]
  Media --> Out["Serve / publish RC URL"]
```

User navigation mirrors scripture hierarchy: language → product (file type) → book → chapter. Chapter pages point at CDN URLs under `CDN_BASE_URL`; Orature products assemble Resource Containers under `CDN_BASE_RC_URL` / `RC_TEMP_DIR`, using template RCs from storage and media from the content tree.

## Pipeline workers

```mermaid
flowchart TB
  FTPDir["FTP / content root"] --> Glob["app.py: glob all files"]
  Glob --> Ch["ChapterWorker<br/>chapter WAV → verse WAV + MP3"]
  Ch --> Vs["VerseWorker<br/>verse WAV → MP3"]
  Vs --> Tr["TrWorker<br/>group verses → .tr packages"]
  Tr --> Bk["BookWorker<br/>combine verses → book WAV/MP3"]
  Bk --> Report["Pipeline report"]
  Report --> Queue["Azure Service Bus messages"]

  subgraph side["Side process"]
    Upd["update_repo.py<br/>clone/pull GL Orature repos"]
  end

  Upd --> RepoDir["ORATURE_REPO_DIR"]
```

Workers run on a timer (`-hr` / `-mn`), share a mutable set of paths across a cycle, and skip unchanged files via content hashes. Tools under `fetcher-pipeline/tools` handle splitting, MP3 conversion, and TR creation (Java/Node helpers alongside Python).

## Design notes

| Topic | Approach |
|--------|----------|
| **Purpose** | Browse and download source audio (and Orature RCs) for translation; process uploaded chapter/verse WAV into CDN-ready formats. |
| **Web stack** | Kotlin 11, Ktor + Netty, Thymeleaf, Koin DI, Shadow JAR (`bible-translation-tools_fetcher.jar`). |
| **Pipeline stack** | Python 3.8+, scheduled workers; depends on Java 11 and Node 14 for conversion tools. |
| **Products** | `mp3`, `wav`, `tr` (BTTR), `orature` (RC zip). |
| **Languages** | UnfoldingWord catalogs for gateway (GL) and heart (HL) languages; UI i18n via Crowdin. |
| **Source text / RCs** | Primary git repos from BIEL GraphQL; RC packaging with `kotlin-resource-container` + `rcmediadownloader`. |
| **Ops** | Root `makefile` builds both images and runs `dockerstack`; images published via GitHub Actions. |

## Related repositories

- Source: [Bible-Translation-Tools/Fetcher](https://github.com/Bible-Translation-Tools/Fetcher)
- Companion consumer: [Bible-Translation-Tools/Orature](https://github.com/Bible-Translation-Tools/Orature) (imports Resource Containers with source audio)
- Resource Container spec: [Door43 Resource Container](https://resource-container.readthedocs.io/)

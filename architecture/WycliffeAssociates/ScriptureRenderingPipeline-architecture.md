# ScriptureRenderingPipeline architecture

[WycliffeAssociates/ScriptureRenderingPipeline](https://github.com/WycliffeAssociates/ScriptureRenderingPipeline) — A rendering pipeline for scripture.

A rendering pipeline for scripture and BTTWriter catalog

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ScriptureRenderingPipeline"]
    M0[".github"]
    M1[".vscode"]
    M2["BTTWriterCatalog"]
    M3["CreateVerseCountsFromRepo"]
    M4["infra"]
    M5["PipelineCommon"]
    M6["ScriptureRenderingPipeline"]
    M7["ScriptureRenderingPipelineWorker"]
    M8["SRPTests"]
    M9["VerseReportingProcessor"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ScriptureRenderingPipeline<br/>A rendering pipeline for scripture"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["BTTWriterCatalog"]
    D3["CreateVerseCountsFromRepo"]
    D4["infra"]
    D5["PipelineCommon"]
    D6["ScriptureRenderingPipeline"]
    D7["ScriptureRenderingPipelineWorker"]
    D8["SRPTests"]
    D9["VerseReportingProcessor"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
  Root --> D9
```

**Directories:** `.github`, `.vscode`, `BTTWriterCatalog`, `CreateVerseCountsFromRepo`, `infra`, `PipelineCommon`, `ScriptureRenderingPipeline`, `ScriptureRenderingPipelineWorker`, `SRPTests`, `VerseReportingProcessor`

**Notable files:** `.dockerignore`, `.gitignore`, `LICENSE`, `README.md`, `ScriptureRenderingPipeline.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["ScriptureRenderingPipeline"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 173 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ScriptureRenderingPipeline](https://github.com/WycliffeAssociates/ScriptureRenderingPipeline)
- Branch analyzed: `master`

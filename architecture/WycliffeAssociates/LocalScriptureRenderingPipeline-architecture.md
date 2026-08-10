# LocalScriptureRenderingPipeline architecture

[WycliffeAssociates/LocalScriptureRenderingPipeline](https://github.com/WycliffeAssociates/LocalScriptureRenderingPipeline) — Run the scripture rendering pipeline locally.

Run the scripture rendering pipeline locally

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["LocalScriptureRenderingPipeline"]
    M0["samplerepos"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: YAML"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["LocalScriptureRenderingPipeline<br/>Run the scripture rendering pipeline locally"]

  subgraph structure["Top-level layout"]
    D0["samplerepos"]
  end

  Root --> D0
```

**Directories:** `samplerepos`

**Notable files:** `.gitignore`, `docker-compose.yml`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["LocalScriptureRenderingPipeline"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/LocalScriptureRenderingPipeline](https://github.com/WycliffeAssociates/LocalScriptureRenderingPipeline)
- Branch analyzed: `master`

# LintingResultsViewer architecture

[WycliffeAssociates/LintingResultsViewer](https://github.com/WycliffeAssociates/LintingResultsViewer) — _no GitHub description_.

A web application for viewing and managing linting results for repositories. The application provides a user interface to browse linting results and receives new linting data via Azure Service Bus messaging.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["LintingResultsViewer"]
    M0[".github"]
    M1["LintingResults"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker, .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["LintingResultsViewer<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["LintingResults"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `LintingResults`

**Notable files:** `.dockerignore`, `.gitignore`, `build_push.sh`, `docker-compose.yml`, `LICENSE`, `LintingResults.sln`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["LintingResultsViewer"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 30 files |
| CSS | 1 files |
| Shell | 1 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker, .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/LintingResultsViewer](https://github.com/WycliffeAssociates/LintingResultsViewer)
- Branch analyzed: `master`

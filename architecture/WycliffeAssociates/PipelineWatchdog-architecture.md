# PipelineWatchdog architecture

[WycliffeAssociates/PipelineWatchdog](https://github.com/WycliffeAssociates/PipelineWatchdog) — _no GitHub description_.

This tool listens to the main rendering pipeline bus and records all of the repos it has seen. It will then on a schedule check all of the repos in WACS against what it has seen and then sends repos to the pipeline again to make sure the creation is handled or the delte is handled.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["PipelineWatchdog"]
    M0[".github"]
    M1["Core"]
    M2["Implementation"]
    M3["Logic"]
    M4["PipelineWatchdog"]
    M5["Telemetry"]
    M6["Tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker, .NET / C#"]
    Lang["Primary language: C#"]
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
  Root["PipelineWatchdog<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["Core"]
    D2["Implementation"]
    D3["Logic"]
    D4["PipelineWatchdog"]
    D5["Telemetry"]
    D6["Tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
```

**Directories:** `.github`, `Core`, `Implementation`, `Logic`, `PipelineWatchdog`, `Telemetry`, `Tests`

**Notable files:** `.dockerignore`, `.gitignore`, `docker-compose.yml`, `PipelineWatchdog.sln`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["PipelineWatchdog"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 21 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker, .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/PipelineWatchdog](https://github.com/WycliffeAssociates/PipelineWatchdog)
- Branch analyzed: `master`

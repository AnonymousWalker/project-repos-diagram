# ScriptureAppBuilder-pipeline architecture

[Bible-Translation-Tools/ScriptureAppBuilder-pipeline](https://github.com/Bible-Translation-Tools/ScriptureAppBuilder-pipeline) — _no GitHub description_.

ScriptureAppBuilder-pipeline is a public repository under Bible-Translation-Tools.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ScriptureAppBuilder-pipeline"]
    M0["appbuilderrunner"]
    M1["appfilemover"]
    M2["ContainerImage"]
    M3["TriggerFunction"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: XML"]
    Lang["Primary language: XML"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ScriptureAppBuilder-pipeline<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["appbuilderrunner"]
    D1["appfilemover"]
    D2["ContainerImage"]
    D3["TriggerFunction"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `appbuilderrunner`, `appfilemover`, `ContainerImage`, `TriggerFunction`

**Notable files:** `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["ScriptureAppBuilder-pipeline"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 1 files |
| Shell | 1 files |
| JavaScript | 1 files |
| PowerShell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | XML |
| **Default branch** | `base` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/ScriptureAppBuilder-pipeline](https://github.com/Bible-Translation-Tools/ScriptureAppBuilder-pipeline)
- Branch analyzed: `base`

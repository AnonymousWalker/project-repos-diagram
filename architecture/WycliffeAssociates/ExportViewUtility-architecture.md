# ExportViewUtility architecture

[WycliffeAssociates/ExportViewUtility](https://github.com/WycliffeAssociates/ExportViewUtility) — A utility to email a view from Dynamics CRM.

This was an internal tool to fufill the need of emailing a csv file of all of the records in a view. The tool uses a fetchxml query to gather the data and then sends them through a configured smtp server

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ExportViewUtility"]
    M0["ExportViewUtility"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ExportViewUtility<br/>A utility to email a view from Dynamics CRM"]

  subgraph structure["Top-level layout"]
    D0["ExportViewUtility"]
  end

  Root --> D0
```

**Directories:** `ExportViewUtility`

**Notable files:** `.gitignore`, `ExportViewUtility.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["ExportViewUtility"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 4 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ExportViewUtility](https://github.com/WycliffeAssociates/ExportViewUtility)
- Branch analyzed: `master`

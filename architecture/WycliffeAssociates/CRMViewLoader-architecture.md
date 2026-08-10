# CRMViewLoader architecture

[WycliffeAssociates/CRMViewLoader](https://github.com/WycliffeAssociates/CRMViewLoader) — A view loader for Dynamics CRM.

A view loader for Dynamics CRM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMViewLoader"]
    M0["CRMViewLoader"]
    M1["CRMViewLoaderTests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["CRMViewLoader<br/>A view loader for Dynamics CRM"]

  subgraph structure["Top-level layout"]
    D0["CRMViewLoader"]
    D1["CRMViewLoaderTests"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `CRMViewLoader`, `CRMViewLoaderTests`

**Notable files:** `.gitignore`, `CRMViewLoader.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMViewLoader"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 8 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/CRMViewLoader](https://github.com/WycliffeAssociates/CRMViewLoader)
- Branch analyzed: `master`

# CRMAssemblyLoader architecture

[WycliffeAssociates/CRMAssemblyLoader](https://github.com/WycliffeAssociates/CRMAssemblyLoader) — An assembly CD tool for Dynamics CRM.

An assembly CD tool for Dynamics CRM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMAssemblyLoader"]
    M0[".github"]
    M1["CRMAssemblyLoader"]
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
  Root["CRMAssemblyLoader<br/>An assembly CD tool for Dynamics CRM"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["CRMAssemblyLoader"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `CRMAssemblyLoader`

**Notable files:** `.gitignore`, `CRMAssemblyLoader.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMAssemblyLoader"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/CRMAssemblyLoader](https://github.com/WycliffeAssociates/CRMAssemblyLoader)
- Branch analyzed: `master`

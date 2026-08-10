# CRMUtils architecture

[WycliffeAssociates/CRMUtils](https://github.com/WycliffeAssociates/CRMUtils) — A set of utilities for interacting with Dynamics CRM.

A set of utilities for interacting with Dynamics CRM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMUtils"]
    M0["CRMUtils"]
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
  Root["CRMUtils<br/>A set of utilities for interacting with Dynamics CRM"]

  subgraph structure["Top-level layout"]
    D0["CRMUtils"]
  end

  Root --> D0
```

**Directories:** `CRMUtils`

**Notable files:** `.gitignore`, `CRMUtils.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMUtils"]
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

- Source: [WycliffeAssociates/CRMUtils](https://github.com/WycliffeAssociates/CRMUtils)
- Branch analyzed: `master`

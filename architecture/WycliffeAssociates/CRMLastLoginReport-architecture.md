# CRMLastLoginReport architecture

[WycliffeAssociates/CRMLastLoginReport](https://github.com/WycliffeAssociates/CRMLastLoginReport) — A utility to generate a report of when somebody last logged into Dynamics CRM.

A utility to generate a report of when somebody last logged into Dynamics CRM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMLastLoginReport"]
    M0[".github"]
    M1["CRMLastLoginReport"]
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
  Root["CRMLastLoginReport<br/>A utility to generate a report of when somebody last logged into Dynamics CRM"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["CRMLastLoginReport"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `CRMLastLoginReport`

**Notable files:** `.gitignore`, `CRMLastLoginReport.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMLastLoginReport"]
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

- Source: [WycliffeAssociates/CRMLastLoginReport](https://github.com/WycliffeAssociates/CRMLastLoginReport)
- Branch analyzed: `master`

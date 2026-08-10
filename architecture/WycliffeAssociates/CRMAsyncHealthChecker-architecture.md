# CRMAsyncHealthChecker architecture

[WycliffeAssociates/CRMAsyncHealthChecker](https://github.com/WycliffeAssociates/CRMAsyncHealthChecker) — A utility to check the amount of async operations waiting and alert if they are above a limit.

A utility to check the amount of async operations waiting in Microsoft Dataverse (formerly Dynamics 365/CRM) and alert if they are above a limit.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMAsyncHealthChecker"]
    M0[".github"]
    M1["CRMAsyncHealthChecker"]
    M2["CRMAsynHealthCheckerTests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["CRMAsyncHealthChecker<br/>A utility to check the amount of async operations waiting and alert if they are "]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["CRMAsyncHealthChecker"]
    D2["CRMAsynHealthCheckerTests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `CRMAsyncHealthChecker`, `CRMAsynHealthCheckerTests`

**Notable files:** `.gitignore`, `CRMAsyncHealthChecker.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMAsyncHealthChecker"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 7 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/CRMAsyncHealthChecker](https://github.com/WycliffeAssociates/CRMAsyncHealthChecker)
- Branch analyzed: `master`

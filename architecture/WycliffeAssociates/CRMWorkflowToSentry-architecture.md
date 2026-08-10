# CRMWorkflowToSentry architecture

[WycliffeAssociates/CRMWorkflowToSentry](https://github.com/WycliffeAssociates/CRMWorkflowToSentry) — Send failed workflows to sentry.

Send failed workflows to sentry

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMWorkflowToSentry"]
    M0[".github"]
    M1["CRMWorkflowToSentry"]
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
  Root["CRMWorkflowToSentry<br/>Send failed workflows to sentry"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["CRMWorkflowToSentry"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `CRMWorkflowToSentry`

**Notable files:** `.gitignore`, `CRMWorkflowToSentry.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMWorkflowToSentry"]
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

- Source: [WycliffeAssociates/CRMWorkflowToSentry](https://github.com/WycliffeAssociates/CRMWorkflowToSentry)
- Branch analyzed: `master`

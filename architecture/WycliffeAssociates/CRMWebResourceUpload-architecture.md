# CRMWebResourceUpload architecture

[WycliffeAssociates/CRMWebResourceUpload](https://github.com/WycliffeAssociates/CRMWebResourceUpload) — A utility to upload and create web resources to dynamics crm.

A utility to upload and create web resources to dynamics crm

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMWebResourceUpload"]
    M0[".github"]
    M1["CRMWebResourceUpload"]
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
  Root["CRMWebResourceUpload<br/>A utility to upload and create web resources to dynamics crm"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["CRMWebResourceUpload"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `CRMWebResourceUpload`

**Notable files:** `.gitignore`, `CRMWebResourceUpload.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMWebResourceUpload"]
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

- Source: [WycliffeAssociates/CRMWebResourceUpload](https://github.com/WycliffeAssociates/CRMWebResourceUpload)
- Branch analyzed: `master`

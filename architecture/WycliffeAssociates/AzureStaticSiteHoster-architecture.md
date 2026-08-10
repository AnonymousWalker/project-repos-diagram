# AzureStaticSiteHoster architecture

[WycliffeAssociates/AzureStaticSiteHoster](https://github.com/WycliffeAssociates/AzureStaticSiteHoster) — A small web application to make static websites in local azure storage emulators much better to use.

A small web application to make static websites in local azure storage emulators much better to use

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["AzureStaticSiteHoster"]
    M0["AzureStaticSiteHoster"]
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
  Root["AzureStaticSiteHoster<br/>A small web application to make static websites in local azure storage emulators"]

  subgraph structure["Top-level layout"]
    D0["AzureStaticSiteHoster"]
  end

  Root --> D0
```

**Directories:** `AzureStaticSiteHoster`

**Notable files:** `.gitignore`, `AzureStaticSiteHoster.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["AzureStaticSiteHoster"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/AzureStaticSiteHoster](https://github.com/WycliffeAssociates/AzureStaticSiteHoster)
- Branch analyzed: `master`

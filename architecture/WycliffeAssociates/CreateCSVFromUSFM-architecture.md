# CreateCSVFromUSFM architecture

[WycliffeAssociates/CreateCSVFromUSFM](https://github.com/WycliffeAssociates/CreateCSVFromUSFM) — Create a CSV from a set of USFM files.

Create a CSV from a set of USFM files

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CreateCSVFromUSFM"]
    M0["CreateCSVFromUSFM.Common"]
    M1["CreateCSVFromUSFM.Console"]
    M2["CreateCSVFromUSFM.DesktopApp"]
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
  Root["CreateCSVFromUSFM<br/>Create a CSV from a set of USFM files"]

  subgraph structure["Top-level layout"]
    D0["CreateCSVFromUSFM.Common"]
    D1["CreateCSVFromUSFM.Console"]
    D2["CreateCSVFromUSFM.DesktopApp"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `CreateCSVFromUSFM.Common`, `CreateCSVFromUSFM.Console`, `CreateCSVFromUSFM.DesktopApp`

**Notable files:** `.gitignore`, `CreateCSVFromUSFM.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CreateCSVFromUSFM"]
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

- Source: [WycliffeAssociates/CreateCSVFromUSFM](https://github.com/WycliffeAssociates/CreateCSVFromUSFM)
- Branch analyzed: `master`

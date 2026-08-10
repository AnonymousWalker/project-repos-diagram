# npoi architecture

[WycliffeAssociates/npoi](https://github.com/WycliffeAssociates/npoi) — a .NET library that can read/write Office formats without Microsoft Office installed. No COM+, no interop..

NPOI =================== This project is the .NET version of POI Java project. With NPOI, you can read/write Office 2003/2007 files very easily.<br />

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["npoi"]
    M0["build"]
    M1["examples"]
    M2["logo"]
    M3["main"]
    M4["ooxml"]
    M5["openxml4Net"]
    M6["OpenXmlFormats"]
    M7["scratchpad"]
    M8["solution"]
    M9["testcases"]
    M10["tools"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users --> M10
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["npoi<br/>a .NET library that can read/write Office formats without Microsoft Office insta"]

  subgraph structure["Top-level layout"]
    D0["build"]
    D1["examples"]
    D2["logo"]
    D3["main"]
    D4["ooxml"]
    D5["openxml4Net"]
    D6["OpenXmlFormats"]
    D7["scratchpad"]
    D8["solution"]
    D9["testcases"]
    D10["tools"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
  Root --> D9
  Root --> D10
```

**Directories:** `build`, `examples`, `logo`, `main`, `ooxml`, `openxml4Net`, `OpenXmlFormats`, `scratchpad`, `solution`, `testcases`, `tools`

**Notable files:** `.gitattributes`, `.gitignore`, `.tgitconfig`, `.travis.yml`, `LICENSE`, `Read Me.txt`, `README.md`, `Release Notes.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["npoi"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 2,793 files |
| PowerShell | 3 files |
| XML | 3 files |
| Batch | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/npoi](https://github.com/WycliffeAssociates/npoi)
- Branch analyzed: `master`

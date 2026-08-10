# quick_usfm_converter architecture

[WycliffeAssociates/quick_usfm_converter](https://github.com/WycliffeAssociates/quick_usfm_converter) — A desktop application that converts usfm to html and docx.

Deprecated in favor of https://github.com/Bible-Translation-Tools/USFM-Converter

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["quick_usfm_converter"]
    M0[".github"]
    M1["USFM_Converter"]
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
  Root["quick_usfm_converter<br/>A desktop application that converts usfm to html and docx"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["USFM_Converter"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `USFM_Converter`

**Notable files:** `.gitignore`, `appveyor.yml`, `installerscript.iss`, `readme.md`, `release.sh`, `USFM_Converter.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["quick_usfm_converter"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 7 files |
| HTML | 1 files |
| CSS | 1 files |
| YAML | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/quick_usfm_converter](https://github.com/WycliffeAssociates/quick_usfm_converter)
- Branch analyzed: `master`

# quick_usfm_converter_console architecture

[WycliffeAssociates/quick_usfm_converter_console](https://github.com/WycliffeAssociates/quick_usfm_converter_console) — _no GitHub description_.

Converts USFM formated files into HTML files. > Can be editted in the Microsoft Word or Libre Office text editors

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["quick_usfm_converter_console"]
    M0[".github"]
    M1["UsfmConverterConsole"]
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
  Root["quick_usfm_converter_console<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["UsfmConverterConsole"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `UsfmConverterConsole`

**Notable files:** `.gitignore`, `installerscript.iss`, `readme.md`, `release.sh`, `UsfmConverterConsole.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["quick_usfm_converter_console"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 3 files |
| HTML | 1 files |
| CSS | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/quick_usfm_converter_console](https://github.com/WycliffeAssociates/quick_usfm_converter_console)
- Branch analyzed: `master`

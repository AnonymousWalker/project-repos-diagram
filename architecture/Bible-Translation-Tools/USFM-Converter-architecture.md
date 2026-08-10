# USFM-Converter architecture

[Bible-Translation-Tools/USFM-Converter](https://github.com/Bible-Translation-Tools/USFM-Converter) — Tool for converting USFM to readable formats like HTML and DOCX.

Tool for converting USFM to readable formats like HTML and DOCX.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFM-Converter"]
    M0[".github"]
    M1["USFMConverter"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["USFM-Converter<br/>Tool for converting USFM to readable formats like HTML and DOCX"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["USFMConverter"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `USFMConverter`

**Notable files:** `.gitignore`, `CHANGELOG.md`, `installerscript.iss`, `README.md`, `usfm-dmg-bg.png`, `usfmconverter.desktop`, `usfmconverter.entitlements`, `usfmconverter.icns`, `usfmconverter.install4j`, `usfmicon.png`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["USFM-Converter"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 33 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | C# |
| **Default branch** | `release` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/USFM-Converter](https://github.com/Bible-Translation-Tools/USFM-Converter)
- Branch analyzed: `release`

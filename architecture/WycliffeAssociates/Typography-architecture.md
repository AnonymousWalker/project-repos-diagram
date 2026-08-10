# Typography architecture

[WycliffeAssociates/Typography](https://github.com/WycliffeAssociates/Typography) — C# Font Reader (TrueType / OpenType / OpenFont / CFF / woff / woff2) , Glyphs Layout and Rendering.

===========

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Typography"]
    M0["Build"]
    M1["Demo"]
    M2["Docs"]
    M3["PixelFarm"]
    M4["PixelFarm.Typography"]
    M5["Typography.GlyphLayout"]
    M6["Typography.OpenFont"]
    M7["Typography.TextBreak"]
    M8["Typography.TextFlow"]
    M9["Typography.TextServices"]
    M10["Unpack_SH"]
    M11["x_autogen2"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
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
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Typography<br/>C# Font Reader (TrueType / OpenType / OpenFont / CFF / woff / woff2) , Glyphs La"]

  subgraph structure["Top-level layout"]
    D0["Build"]
    D1["Demo"]
    D2["Docs"]
    D3["PixelFarm"]
    D4["PixelFarm.Typography"]
    D5["Typography.GlyphLayout"]
    D6["Typography.OpenFont"]
    D7["Typography.TextBreak"]
    D8["Typography.TextFlow"]
    D9["Typography.TextServices"]
    D10["Unpack_SH"]
    D11["x_autogen2"]
    D12["x_autogen_netstandard2.0"]
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
  Root --> D11
  Root --> D12
```

**Directories:** `Build`, `Demo`, `Docs`, `PixelFarm`, `PixelFarm.Typography`, `Typography.GlyphLayout`, `Typography.OpenFont`, `Typography.TextBreak`, `Typography.TextFlow`, `Typography.TextServices`, `Unpack_SH`, `x_autogen2`, `x_autogen_netstandard2.0`

**Notable files:** `.gitattributes`, `.gitignore`, `LICENSE.md`, `OLD_README.md`, `README.md`, `Typography.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["Typography"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 830 files |
| HTML | 76 files |
| XML | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/Typography](https://github.com/WycliffeAssociates/Typography)
- Branch analyzed: `master`

# BTTWriterLib architecture

[WycliffeAssociates/BTTWriterLib](https://github.com/WycliffeAssociates/BTTWriterLib) — A set of utilities for Reading files from Bible Translation Tools Writer.

A set of utilities for Reading files from Bible Translation Tools Writer

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTTWriterLib"]
    M0[".github"]
    M1["BTTWriterLib"]
    M2["BTTWriterLibTests"]
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
  Root["BTTWriterLib<br/>A set of utilities for Reading files from Bible Translation Tools Writer"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["BTTWriterLib"]
    D2["BTTWriterLibTests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `BTTWriterLib`, `BTTWriterLibTests`

**Notable files:** `.gitignore`, `BTTWriterLib.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["BTTWriterLib"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 14 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/BTTWriterLib](https://github.com/WycliffeAssociates/BTTWriterLib)
- Branch analyzed: `master`

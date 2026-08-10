# ScriptureBurrito architecture

[WycliffeAssociates/ScriptureBurrito](https://github.com/WycliffeAssociates/ScriptureBurrito) — Library for serializing and deserializing scripture burritos.

Library for serializing and deserializing scripture burritos

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ScriptureBurrito"]
    M0[".github"]
    M1["ScriptureBurrito"]
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
  Root["ScriptureBurrito<br/>Library for serializing and deserializing scripture burritos"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["ScriptureBurrito"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `ScriptureBurrito`

**Notable files:** `.gitignore`, `global.json`, `LICENSE`, `README.md`, `ScriptureBurrito.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["ScriptureBurrito"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 19 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ScriptureBurrito](https://github.com/WycliffeAssociates/ScriptureBurrito)
- Branch analyzed: `master`

# USFMDebugger architecture

[WycliffeAssociates/USFMDebugger](https://github.com/WycliffeAssociates/USFMDebugger) — An application that gives a graphical tree view of how USFMToolsSharp understands a particular USFM document.

An application that gives a graphical tree view of how USFMToolsSharp understands a particular USFM document

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMDebugger"]
    M0["USFMToolsSharpDebugger"]
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
  Root["USFMDebugger<br/>An application that gives a graphical tree view of how USFMToolsSharp understand"]

  subgraph structure["Top-level layout"]
    D0["USFMToolsSharpDebugger"]
  end

  Root --> D0
```

**Directories:** `USFMToolsSharpDebugger`

**Notable files:** `.gitignore`, `LICENSE`, `README.md`, `USFMToolsSharpDebugger.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMDebugger"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMDebugger](https://github.com/WycliffeAssociates/USFMDebugger)
- Branch analyzed: `master`

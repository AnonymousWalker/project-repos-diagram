# ScriptureTemplates architecture

[WycliffeAssociates/ScriptureTemplates](https://github.com/WycliffeAssociates/ScriptureTemplates) — Templates for read.bibletranslationtools.org.

Templates for read.bibletranslationtools.org

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ScriptureTemplates"]
    M0["css"]
    M1["fonts"]
    M2["js"]
    M3["templates"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: JavaScript"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ScriptureTemplates<br/>Templates for read.bibletranslationtools.org"]

  subgraph structure["Top-level layout"]
    D0["css"]
    D1["fonts"]
    D2["js"]
    D3["templates"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `css`, `fonts`, `js`, `templates`

**Notable files:** `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["ScriptureTemplates"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 27 files |
| CSS | 13 files |
| HTML | 6 files |
| TypeScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | JavaScript |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ScriptureTemplates](https://github.com/WycliffeAssociates/ScriptureTemplates)
- Branch analyzed: `master`

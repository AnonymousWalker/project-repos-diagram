# interpresure_scripture_analysis architecture

[Bible-Translation-Tools/interpresure_scripture_analysis](https://github.com/Bible-Translation-Tools/interpresure_scripture_analysis) — Agentic analysis of translation drafts.

Agentic analysis of translation drafts

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["interpresure_scripture_analysis"]
    M0[".vscode"]
    M1["src"]
    M2["viewer"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["interpresure_scripture_analysis<br/>Agentic analysis of translation drafts"]

  subgraph structure["Top-level layout"]
    D0[".vscode"]
    D1["src"]
    D2["viewer"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.vscode`, `src`, `viewer`

**Notable files:** `.gitattributes`, `.gitignore`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["interpresure_scripture_analysis"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 17 files |
| JavaScript | 5 files |
| CSS | 2 files |
| HTML | 1 files |
| YAML | 1 files |
| TypeScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/interpresure_scripture_analysis](https://github.com/Bible-Translation-Tools/interpresure_scripture_analysis)
- Branch analyzed: `main`

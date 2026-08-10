# 8woc2018_reversi architecture

[WycliffeAssociates/8woc2018_reversi](https://github.com/WycliffeAssociates/8woc2018_reversi) — Reversi challenge for 8woc 2018.

Reversi Challenge =================

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["8woc2018_reversi"]
    M0["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["8woc2018_reversi<br/>Reversi challenge for 8woc 2018"]

  subgraph structure["Top-level layout"]
    D0["tests"]
  end

  Root --> D0
```

**Directories:** `tests`

**Notable files:** `.gitignore`, `example_input.json`, `example_output.json`, `example_solution_template.py`, `README.md`, `tester.py`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["8woc2018_reversi"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/8woc2018_reversi](https://github.com/WycliffeAssociates/8woc2018_reversi)
- Branch analyzed: `master`

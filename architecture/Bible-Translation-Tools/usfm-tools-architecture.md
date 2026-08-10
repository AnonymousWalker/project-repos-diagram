# usfm-tools architecture

[Bible-Translation-Tools/usfm-tools](https://github.com/Bible-Translation-Tools/usfm-tools) — Tools for converting, cleaning, and checking Scripture text.

Tools for converting, cleaning, and checking Scripture text

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["usfm-tools"]
    M0["misc"]
    M1["src"]
    M2["tests"]
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
  Root["usfm-tools<br/>Tools for converting, cleaning, and checking Scripture text"]

  subgraph structure["Top-level layout"]
    D0["misc"]
    D1["src"]
    D2["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `misc`, `src`, `tests`

**Notable files:** `.gitignore`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["usfm-tools"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 89 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `default` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/usfm-tools](https://github.com/Bible-Translation-Tools/usfm-tools)
- Branch analyzed: `default`

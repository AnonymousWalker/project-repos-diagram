# SpeechToText architecture

[WycliffeAssociates/SpeechToText](https://github.com/WycliffeAssociates/SpeechToText) — _no GitHub description_.

SpeechToText is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["SpeechToText"]
    M0["server"]
    M1["stt-ui"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["SpeechToText<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["server"]
    D1["stt-ui"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `server`, `stt-ui`

**Notable files:** `.gitignore`, `docker-compose.yml`, `run.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["SpeechToText"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 5 files |
| JavaScript | 3 files |
| YAML | 2 files |
| Python | 2 files |
| CSS | 2 files |
| Shell | 1 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/SpeechToText](https://github.com/WycliffeAssociates/SpeechToText)
- Branch analyzed: `master`

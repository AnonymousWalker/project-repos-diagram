# AudioSABbuilder architecture

[WycliffeAssociates/AudioSABbuilder](https://github.com/WycliffeAssociates/AudioSABbuilder) — python app for making an Android app out of chapter based Scripture Audio mp3s.

python app for making an Android app out of chapter based Scripture Audio mp3s

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["AudioSABbuilder"]
    M0["resources"]
    M1["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["AudioSABbuilder<br/>python app for making an Android app out of chapter based Scripture Audio mp3s"]

  subgraph structure["Top-level layout"]
    D0["resources"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `resources`, `src`

**Notable files:** `.gitattributes`, `.gitignore`, `LICENSE`, `README.md`, `requirements.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["AudioSABbuilder core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 6 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/AudioSABbuilder](https://github.com/WycliffeAssociates/AudioSABbuilder)
- Branch analyzed: `master`

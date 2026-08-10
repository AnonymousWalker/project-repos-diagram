# bible_getter architecture

[WycliffeAssociates/bible_getter](https://github.com/WycliffeAssociates/bible_getter) — Get bible in usfm format from wordproject.org and bible.com.

These scripts help to get bible in usfm format from wordproject.org and bible.com

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["bible_getter"]
    F0["get_bible.com.py"]
    F1["get_wordproject.org.py"]
    F2["README.md"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["bible_getter<br/>Get bible in usfm format from wordproject.org and bible.com"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `get_bible.com.py`, `get_wordproject.org.py`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["bible_getter"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/bible_getter](https://github.com/WycliffeAssociates/bible_getter)
- Branch analyzed: `master`

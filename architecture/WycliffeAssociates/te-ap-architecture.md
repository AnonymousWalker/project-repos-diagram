# te-ap architecture

[WycliffeAssociates/te-ap](https://github.com/WycliffeAssociates/te-ap) — Translation Exchange Docker files for the Access Point container.

moved to https://github.com/Bible-Translation-Tools/BTT-Exchanger

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["te-ap"]
    F0["Dockerfile"]
    F1["entrypoint.sh"]
    F2["hostapd"]
    F3["README.md"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: Shell"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users --> F3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["te-ap<br/>Translation Exchange Docker files for the Access Point container"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `Dockerfile`, `entrypoint.sh`, `hostapd`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["te-ap"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/te-ap](https://github.com/WycliffeAssociates/te-ap)
- Branch analyzed: `master`

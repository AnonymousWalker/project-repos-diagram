# brightcove-api-vidoes-list architecture

[WycliffeAssociates/brightcove-api-vidoes-list](https://github.com/WycliffeAssociates/brightcove-api-vidoes-list) — Fall Hackathon 2022 project to download list of videos from Brigthcove api.

Fall Hackathon 2022 project to download list of videos from Brigthcove api

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["brightcove-api-vidoes-list"]
    F0[".gitignore"]
    F1["index.js"]
    F2["LICENSE"]
    F3["package-lock.json"]
    F4["package.json"]
    F5["README.md"]
    F6["videos_data.json"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users --> F3
  Users --> F4
  Users --> F5
  Users --> F6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["brightcove-api-vidoes-list<br/>Fall Hackathon 2022 project to download list of videos from Brigthcove api"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `.gitignore`, `index.js`, `LICENSE`, `package-lock.json`, `package.json`, `README.md`, `videos_data.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["brightcove-api-vidoes-list"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/brightcove-api-vidoes-list](https://github.com/WycliffeAssociates/brightcove-api-vidoes-list)
- Branch analyzed: `master`

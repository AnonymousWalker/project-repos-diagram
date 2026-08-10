# ExtractLetters architecture

[WycliffeAssociates/ExtractLetters](https://github.com/WycliffeAssociates/ExtractLetters) — 8Woc 2017 Mini Project.

8Woc 2017 Mini Project

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ExtractLetters"]
    M0[".kdev4"]
    M1["build"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: C++"]
    Lang["Primary language: C++"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ExtractLetters<br/>8Woc 2017 Mini Project"]

  subgraph structure["Top-level layout"]
    D0[".kdev4"]
    D1["build"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.kdev4`, `build`

**Notable files:** `.gitattributes`, `.gitignore`, `CMakeLists.txt`, `ExtractLetters.kdev4`, `json.hpp`, `main.cpp`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["ExtractLetters"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C++ | 3 files |
| C | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | C++ |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ExtractLetters](https://github.com/WycliffeAssociates/ExtractLetters)
- Branch analyzed: `master`

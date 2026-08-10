# USFMToolsDart architecture

[WycliffeAssociates/USFMToolsDart](https://github.com/WycliffeAssociates/USFMToolsDart) — A port of USFMToolsSharp to the Dart language.

A port of USFMToolsSharp to the Dart language

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsDart"]
    M0["lib"]
    M1["test"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Flutter / Dart"]
    Lang["Primary language: Dart"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["USFMToolsDart<br/>A port of USFMToolsSharp to the Dart language"]

  subgraph structure["Top-level layout"]
    D0["lib"]
    D1["test"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `lib`, `test`

**Notable files:** `.gitignore`, `analysis_options.yaml`, `LICENSE`, `pubspec.yaml`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  UI["Flutter UI"] --> App["USFMToolsDart"]
  App --> Platform["iOS / Android / desktop"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Dart | 6 files |
| YAML | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Flutter / Dart |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsDart](https://github.com/WycliffeAssociates/USFMToolsDart)
- Branch analyzed: `master`

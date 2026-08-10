# android-gogs-ui architecture

[WycliffeAssociates/android-gogs-ui](https://github.com/WycliffeAssociates/android-gogs-ui) — UI for login and profile creation for Door43 gogs.

UI for login and profile creation for Door43 gogs

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["android-gogs-ui"]
    M0["com.door43.tools.reporting"]
    M1["door43login"]
    M2["sysutils"]
    M3["widgets"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: XML"]
    Lang["Primary language: XML"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["android-gogs-ui<br/>UI for login and profile creation for Door43 gogs"]

  subgraph structure["Top-level layout"]
    D0["com.door43.tools.reporting"]
    D1["door43login"]
    D2["sysutils"]
    D3["widgets"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `com.door43.tools.reporting`, `door43login`, `sysutils`, `widgets`

**Notable files:** `.gitignore`, `COPYING`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["android-gogs-ui"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| XML | 35 files |
| Java | 34 files |
| Gradle | 4 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | XML |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/android-gogs-ui](https://github.com/WycliffeAssociates/android-gogs-ui)
- Branch analyzed: `master`

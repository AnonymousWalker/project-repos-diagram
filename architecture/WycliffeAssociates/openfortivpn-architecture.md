# openfortivpn architecture

[WycliffeAssociates/openfortivpn](https://github.com/WycliffeAssociates/openfortivpn) — Client for PPP+SSL VPN tunnel services.

openfortivpn ============

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["openfortivpn"]
    M0[".github"]
    M1["doc"]
    M2["etc"]
    M3["lib"]
    M4["src"]
    M5["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: C"]
    Lang["Primary language: C"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["openfortivpn<br/>Client for PPP+SSL VPN tunnel services"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["doc"]
    D2["etc"]
    D3["lib"]
    D4["src"]
    D5["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.github`, `doc`, `etc`, `lib`, `src`, `tests`

**Notable files:** `.gitignore`, `autogen.sh`, `CHANGELOG.md`, `configure.ac`, `LICENSE`, `LICENSE.OpenSSL`, `Makefile.am`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["openfortivpn"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C | 22 files |
| Shell | 6 files |
| Python | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | C |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/openfortivpn](https://github.com/WycliffeAssociates/openfortivpn)
- Branch analyzed: `master`

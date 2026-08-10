# usfm-scanner architecture

[WycliffeAssociates/usfm-scanner](https://github.com/WycliffeAssociates/usfm-scanner) — _no GitHub description_.

Deprecated in favor of https://github.com/WycliffeAssociates/USFMScannerNet

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["usfm-scanner"]
    M0[".github"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: Shell"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["usfm-scanner<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
  end

  Root --> D0
```

**Directories:** `.github`

**Notable files:** `.gitignore`, `.gitmodules`, `build_push.sh`, `docker-compose.yml`, `Dockerfile`, `entry.sh`, `ErrorCodes.csv`, `LICENSE`, `listener.py`, `README.md`, `requirements.txt`, `usfmtools`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["usfm-scanner core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 2 files |
| YAML | 1 files |
| Python | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python, Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/usfm-scanner](https://github.com/WycliffeAssociates/usfm-scanner)
- Branch analyzed: `master`

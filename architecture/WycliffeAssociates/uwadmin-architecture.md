# uwadmin architecture

[WycliffeAssociates/uwadmin](https://github.com/WycliffeAssociates/uwadmin) — Code for uW Admin site.

1. `pip install -r requirements.txt` 2. `./manage.py syncdb` 3. `./manage.py loaddata sites`

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["uwadmin"]
    M0["fixtures"]
    M1["uwadmin"]
    M2["uwutils"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["uwadmin<br/>Code for uW Admin site"]

  subgraph structure["Top-level layout"]
    D0["fixtures"]
    D1["uwadmin"]
    D2["uwutils"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `fixtures`, `uwadmin`, `uwutils`

**Notable files:** `.gitignore`, `LICENSE`, `manage.py`, `README.md`, `requirements.txt`, `tox.ini`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["uwadmin core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 49 files |
| Python | 32 files |
| HTML | 23 files |
| CSS | 3 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/uwadmin](https://github.com/WycliffeAssociates/uwadmin)
- Branch analyzed: `master`

# translationDatabaseWeb architecture

[WycliffeAssociates/translationDatabaseWeb](https://github.com/WycliffeAssociates/translationDatabaseWeb) — _no GitHub description_.

translationDatabase ===================

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["translationDatabaseWeb"]
    M0["fixtures"]
    M1["static"]
    M2["td"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["translationDatabaseWeb<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["fixtures"]
    D1["static"]
    D2["td"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `fixtures`, `static`, `td`

**Notable files:** `.coveragerc`, `.env`, `.gitattributes`, `.gitignore`, `.travis.yml`, `gondor.yml`, `manage.py`, `package.json`, `Procfile`, `readme-dev.md`, `README.md`, `requirements-test.txt`, `requirements.txt`, `rest_api.md`, `tox.ini`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["translationDatabaseWeb core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 235 files |
| HTML | 82 files |
| JavaScript | 8 files |
| YAML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/translationDatabaseWeb](https://github.com/WycliffeAssociates/translationDatabaseWeb)
- Branch analyzed: `master`

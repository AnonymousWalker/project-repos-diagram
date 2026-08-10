# scripture-burrito architecture

[Bible-Translation-Tools/scripture-burrito](https://github.com/Bible-Translation-Tools/scripture-burrito) — Scripture Burrito Schema & Docs 🌯.

This fork documents the Wycliffe Associates usage profile for Scripture Burrito and keeps the validation rules in sync with that profile.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["scripture-burrito"]
    M0[".github"]
    M1["code"]
    M2["docs"]
    M3["logo"]
    M4["schema"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-burrito<br/>Scripture Burrito Schema & Docs 🌯"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["code"]
    D2["docs"]
    D3["logo"]
    D4["schema"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.github`, `code`, `docs`, `logo`, `schema`

**Notable files:** `.gitignore`, `.nojekyll`, `.readthedocs.yaml`, `CNAME`, `CONTRIBUTORS`, `LICENSE`, `package-lock.json`, `package.json`, `README.md`, `requirements.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["scripture-burrito core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 4 files |
| JavaScript | 2 files |
| Shell | 2 files |
| XSLT | 1 files |
| XML | 1 files |
| CSS | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Python |
| **Default branch** | `wycliffe-associates` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/scripture-burrito](https://github.com/Bible-Translation-Tools/scripture-burrito)
- Branch analyzed: `wycliffe-associates`

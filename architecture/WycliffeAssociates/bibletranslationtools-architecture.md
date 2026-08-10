# bibletranslationtools architecture

[WycliffeAssociates/bibletranslationtools](https://github.com/WycliffeAssociates/bibletranslationtools) — _no GitHub description_.

bibletranslationtools is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["bibletranslationtools"]
    M0["wp-admin"]
    M1["wp-content"]
    M2["wp-includes"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: PHP"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["bibletranslationtools<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["wp-admin"]
    D1["wp-content"]
    D2["wp-includes"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `wp-admin`, `wp-content`, `wp-includes`

**Notable files:** `.gitignore`, `.htaccess`, `android-chrome-192x192.png`, `android-chrome-384x384.png`, `apple-touch-icon-120x120.png`, `apple-touch-icon-152x152.png`, `apple-touch-icon-180x180.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-76x76.png`, `apple-touch-icon.png`, `article.aspx`, `azuredeploy.json`, `browserconfig.xml`, `docker-compose.yml`, `example.config.php`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon.ico`, `index.php`, `license.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["bibletranslationtools"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| PHP | 2,038 files |
| JavaScript | 763 files |
| CSS | 436 files |
| SCSS | 78 files |
| TypeScript | 53 files |
| HTML | 25 files |
| XML | 2 files |
| YAML | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/bibletranslationtools](https://github.com/WycliffeAssociates/bibletranslationtools)
- Branch analyzed: `master`

# docker-sentry architecture

[WycliffeAssociates/docker-sentry](https://github.com/WycliffeAssociates/docker-sentry) — Docker Official Image packaging for Sentry.

This is the Git repo of the official Docker image for [sentry](https://registry.hub.docker.com/_/sentry/). See the Hub page for the full readme on how to use the Docker image and for information regarding contributing and issues.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["docker-sentry"]
    M0["8.21"]
    M1["8.22"]
    M2["8.23.0.dev0"]
    M3["git"]
    M4["test"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Shell"]
    Lang["Primary language: Shell"]
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
  Root["docker-sentry<br/>Docker Official Image packaging for Sentry"]

  subgraph structure["Top-level layout"]
    D0["8.21"]
    D1["8.22"]
    D2["8.23.0.dev0"]
    D3["git"]
    D4["test"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `8.21`, `8.22`, `8.23.0.dev0`, `git`, `test`

**Notable files:** `.travis.yml`, `build-git.sh`, `generate-stackbrew-library.sh`, `LICENSE`, `README.md`, `update.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["docker-sentry"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 8 files |
| YAML | 4 files |
| Python | 4 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Shell |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/docker-sentry](https://github.com/WycliffeAssociates/docker-sentry)
- Branch analyzed: `master`

# gosu architecture

[WycliffeAssociates/gosu](https://github.com/WycliffeAssociates/gosu) — Simple Go-based setuid+setgid+setgroups+exec.

This is a simple tool grown out of the simple fact that `su` and `sudo` have very strange and often annoying TTY and signal-forwarding behavior. They're also somewhat complex to setup and use (especially in the case of `sudo`), which allows for a great deal of expressivity, but falls flat if all you need is "run this specific application as this specific user and get out of the pipeline".

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["gosu"]
    F0[".dockerignore"]
    F1[".gitignore"]
    F2[".travis.yml"]
    F3["build.sh"]
    F4["Dockerfile"]
    F5["Dockerfile.test"]
    F6["INSTALL.md"]
    F7["LICENSE"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: Shell"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users --> F3
  Users --> F4
  Users --> F5
  Users --> F6
  Users --> F7
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["gosu<br/>Simple Go-based setuid+setgid+setgroups+exec"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `.dockerignore`, `.gitignore`, `.travis.yml`, `build.sh`, `Dockerfile`, `Dockerfile.test`, `INSTALL.md`, `LICENSE`, `main.go`, `README.md`, `setup-user.go`, `sign.sh`, `test.sh`, `version.go`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["gosu"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 3 files |
| Go | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/gosu](https://github.com/WycliffeAssociates/gosu)
- Branch analyzed: `master`

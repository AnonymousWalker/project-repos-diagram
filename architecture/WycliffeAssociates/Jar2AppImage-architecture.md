# Jar2AppImage architecture

[WycliffeAssociates/Jar2AppImage](https://github.com/WycliffeAssociates/Jar2AppImage) — Generic scripts and documentation to take a fat or shadow jar and make it into a linux AppImage.

Generic scripts and documentation to take a jdk11 fat or shadow jar and make it into a linux AppImage bundled with a jdk11 jre. Uses [linuxdeploy](https://github.com/linuxdeploy/linuxdeploy) and [AdoptOpenJDK 11](https://github.com/AdoptOpenJDK/openjdk11-binaries)

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Jar2AppImage"]
    F0[".gitignore"]
    F1["AppRun"]
    F2["build.sh"]
    F3["icon.svg"]
    F4["LICENSE"]
    F5["README.md"]
    F6["vars.env"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Shell"]
    Lang["Primary language: Shell"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users --> F3
  Users --> F4
  Users --> F5
  Users --> F6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Jar2AppImage<br/>Generic scripts and documentation to take a fat or shadow jar and make it into a"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `.gitignore`, `AppRun`, `build.sh`, `icon.svg`, `LICENSE`, `README.md`, `vars.env`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["Jar2AppImage"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Shell |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/Jar2AppImage](https://github.com/WycliffeAssociates/Jar2AppImage)
- Branch analyzed: `master`

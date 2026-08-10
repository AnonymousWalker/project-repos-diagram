# JoshuaProjectClient architecture

[WycliffeAssociates/JoshuaProjectClient](https://github.com/WycliffeAssociates/JoshuaProjectClient) — A client for the Joshua Project API.

A .NET Standard 2.1 client library for the [Joshua Project API](https://api.joshuaproject.net), providing easy access to data about unreached people groups and languages around the world.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["JoshuaProjectClient"]
    M0[".github"]
    M1["Models"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["JoshuaProjectClient<br/>A client for the Joshua Project API"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["Models"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `Models`

**Notable files:** `.gitignore`, `Client.cs`, `JoshuaProjectClient.csproj`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["JoshuaProjectClient"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 5 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/JoshuaProjectClient](https://github.com/WycliffeAssociates/JoshuaProjectClient)
- Branch analyzed: `master`

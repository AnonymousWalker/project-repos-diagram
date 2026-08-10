# DataverseMetadataMCPServer architecture

[WycliffeAssociates/DataverseMetadataMCPServer](https://github.com/WycliffeAssociates/DataverseMetadataMCPServer) — An MCP server that can be used to query Dataverse/Power Platform metadata.

An MCP (Model Context Protocol) server that provides tools for querying Microsoft Dataverse/Power Platform metadata. This server allows AI assistants like GitHub Copilot to interact with Dataverse environments to retrieve entity and attribute metadata.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["DataverseMetadataMCPServer"]
    M0[".github"]
    M1["DataverseMetadataMCPServer"]
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
  Root["DataverseMetadataMCPServer<br/>An MCP server that can be used to query Dataverse/Power Platform metadata"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["DataverseMetadataMCPServer"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `.github`, `DataverseMetadataMCPServer`

**Notable files:** `.gitignore`, `DataverseMetadataMCPServer.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["DataverseMetadataMCPServer"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/DataverseMetadataMCPServer](https://github.com/WycliffeAssociates/DataverseMetadataMCPServer)
- Branch analyzed: `master`

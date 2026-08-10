# lazvard-message architecture

[WycliffeAssociates/lazvard-message](https://github.com/WycliffeAssociates/lazvard-message) — lightweight AMQP server - Azure Service Bus simulator.

Lazvard Message is an AMQP server simulator that is **unofficially** compatible with Azure Service Bus.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["lazvard-message"]
    M0[".github"]
    M1[".vscode"]
    M2["src"]
    M3["test"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["lazvard-message<br/>lightweight AMQP server - Azure Service Bus simulator"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["src"]
    D3["test"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `.vscode`, `src`, `test`

**Notable files:** `.editorconfig`, `.gitattributes`, `.gitignore`, `Lazvard.Message.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["lazvard-message"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 54 files |
| PowerShell | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/lazvard-message](https://github.com/WycliffeAssociates/lazvard-message)
- Branch analyzed: `main`

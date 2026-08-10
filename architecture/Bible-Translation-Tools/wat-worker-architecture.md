# wat-worker architecture

[Bible-Translation-Tools/wat-worker](https://github.com/Bible-Translation-Tools/wat-worker) — Cloudflare worker app to process singleton words with AI models.

``` npm install npm run dev ```

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["wat-worker"]
    M0["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["wat-worker<br/>Cloudflare worker app to process singleton words with AI models"]

  subgraph structure["Top-level layout"]
    D0["src"]
  end

  Root --> D0
```

**Directories:** `src`

**Notable files:** `.gitignore`, `package-lock.json`, `package.json`, `README.md`, `schema.sql`, `tsconfig.json`, `worker-configuration.d.ts`, `wrangler.jsonc`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["wat-worker"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 3 files |
| SQL | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/wat-worker](https://github.com/Bible-Translation-Tools/wat-worker)
- Branch analyzed: `main`

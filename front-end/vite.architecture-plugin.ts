import fs from "node:fs";
import path from "node:path";
import type { Plugin } from "vite";

export type DocMeta = {
  id: string;
  title: string;
  org: string;
  path: string;
  description: string;
  handAuthored: boolean;
};

function walkMarkdown(dir: string, base: string, out: string[]): void {
  if (!fs.existsSync(dir)) return;
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const rel = path.join(base, name).replace(/\\/g, "/");
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      walkMarkdown(full, rel, out);
    } else if (name.endsWith(".md")) {
      out.push(rel);
    }
  }
}

function parseIndex(indexMd: string): Map<string, { description: string; hand: boolean }> {
  const map = new Map<string, { description: string; hand: boolean }>();
  for (const line of indexMd.split("\n")) {
    const m = line.match(
      /^- \[([^\]]+)\]\(([^)]+)\)(?: \*\(hand-authored\)\*)?(?: — (.+))?$/,
    );
    if (!m) continue;
    const [, , link, description = ""] = m;
    const p = link.replace(/^\.\//, "");
    map.set(p, {
      description: description.trim(),
      hand: line.includes("hand-authored"),
    });
  }
  return map;
}

function buildCatalog(repoRoot: string): DocMeta[] {
  const paths: string[] = [];
  walkMarkdown(path.join(repoRoot, "architecture"), "architecture", paths);

  for (const name of ["Orature-architecture.md", "Fetcher-architecture.md"]) {
    if (fs.existsSync(path.join(repoRoot, name))) paths.push(name);
  }

  const indexPath = path.join(repoRoot, "architecture-index.md");
  const indexMeta = fs.existsSync(indexPath)
    ? parseIndex(fs.readFileSync(indexPath, "utf8"))
    : new Map();

  const entries: DocMeta[] = [];
  for (const rel of paths) {
    if (rel.includes(".sha-cache")) continue;

    if (rel === "Orature-architecture.md" || rel === "Fetcher-architecture.md") {
      const title = rel.replace("-architecture.md", "");
      const extra = indexMeta.get(rel);
      entries.push({
        id: rel,
        title,
        org: "Bible-Translation-Tools",
        path: rel,
        description: extra?.description || "Hand-authored architecture review",
        handAuthored: true,
      });
      continue;
    }

    const match = rel.match(/^architecture\/([^/]+)\/(.+)-architecture\.md$/);
    if (!match) continue;
    const [, org, name] = match;
    const extra = indexMeta.get(rel);
    entries.push({
      id: rel,
      title: name,
      org,
      path: rel,
      description: extra?.description || "",
      handAuthored: Boolean(extra?.hand),
    });
  }

  return entries.sort((a, b) => {
    if (a.handAuthored !== b.handAuthored) return a.handAuthored ? -1 : 1;
    const org = a.org.localeCompare(b.org);
    if (org !== 0) return org;
    return a.title.localeCompare(b.title);
  });
}

const VIRTUAL_ID = "virtual:architecture-docs";
const RESOLVED_ID = "\0" + VIRTUAL_ID;

/**
 * Scans the parent repo for architecture markdown and exposes:
 * - catalog metadata
 * - lazy loaders via /@fs absolute paths (works outside Vite root)
 */
export function architectureDocsPlugin(repoRoot: string): Plugin {
  const root = path.resolve(repoRoot);

  const generate = () => {
    const catalog = buildCatalog(root);
    const loaderEntries = catalog.map((doc) => {
      const abs = path.resolve(root, doc.path).replace(/\\/g, "/");
      // Vite filesystem URL for files outside project root
      return `  ${JSON.stringify(doc.path)}: () => import(${JSON.stringify(`/@fs/${abs}?raw`)}).then((m) => m.default)`;
    });

    // Also allow loading the index if needed later
    const indexAbs = path.resolve(root, "architecture-index.md").replace(/\\/g, "/");
    if (fs.existsSync(path.join(root, "architecture-index.md"))) {
      loaderEntries.push(
        `  "architecture-index.md": () => import(${JSON.stringify(`/@fs/${indexAbs}?raw`)}).then((m) => m.default)`,
      );
    }

    return `export const catalog = ${JSON.stringify(catalog, null, 2)};
export const loaders = {
${loaderEntries.join(",\n")}
};
export async function loadMarkdown(path) {
  const loader = loaders[path];
  if (!loader) return null;
  return loader();
}
`;
  };

  return {
    name: "architecture-docs",
    resolveId(id) {
      if (id === VIRTUAL_ID) return RESOLVED_ID;
      return null;
    },
    load(id) {
      if (id === RESOLVED_ID) return generate();
      return null;
    },
    configureServer(server) {
      const watchRoots = [
        path.join(root, "architecture"),
        path.join(root, "architecture-index.md"),
        path.join(root, "Orature-architecture.md"),
        path.join(root, "Fetcher-architecture.md"),
      ];
      for (const p of watchRoots) {
        if (fs.existsSync(p)) server.watcher.add(p);
      }
      const invalidate = (file: string) => {
        if (!file.replace(/\\/g, "/").includes(root.replace(/\\/g, "/"))) return;
        if (!file.endsWith(".md") && !file.includes(`${path.sep}architecture${path.sep}`)) return;
        const mod = server.moduleGraph.getModuleById(RESOLVED_ID);
        if (mod) {
          server.moduleGraph.invalidateModule(mod);
          server.ws.send({ type: "full-reload" });
        }
      };
      server.watcher.on("add", invalidate);
      server.watcher.on("change", invalidate);
      server.watcher.on("unlink", invalidate);
    },
    buildStart() {
      // Ensure Vite sees these as part of the graph during build via virtual module load
      this.addWatchFile(path.join(root, "architecture-index.md"));
    },
  };
}

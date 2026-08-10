import {
  catalog as virtualCatalog,
  loadMarkdown as virtualLoadMarkdown,
} from "virtual:architecture-docs";

export type DocEntry = {
  id: string;
  title: string;
  org: string;
  path: string;
  description: string;
  handAuthored: boolean;
};

export async function loadMarkdown(path: string): Promise<string | null> {
  return virtualLoadMarkdown(path);
}

export async function buildCatalog(): Promise<DocEntry[]> {
  return virtualCatalog as DocEntry[];
}

export function groupByOrg(entries: DocEntry[]): Map<string, DocEntry[]> {
  const map = new Map<string, DocEntry[]>();
  for (const entry of entries) {
    const list = map.get(entry.org) ?? [];
    list.push(entry);
    map.set(entry.org, list);
  }
  return map;
}

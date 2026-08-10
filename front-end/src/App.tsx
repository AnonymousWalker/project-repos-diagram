import { useEffect, useMemo, useState } from "react";
import { Sidebar } from "./components/Sidebar";
import { MarkdownView } from "./components/MarkdownView";
import { buildCatalog, groupByOrg, loadMarkdown, type DocEntry } from "./lib/catalog";

function readHash(): string | null {
  const raw = window.location.hash.replace(/^#/, "");
  return raw ? decodeURIComponent(raw) : null;
}

export default function App() {
  const [catalog, setCatalog] = useState<DocEntry[]>([]);
  const [loadingCatalog, setLoadingCatalog] = useState(true);
  const [query, setQuery] = useState("");
  const [menuOpen, setMenuOpen] = useState(false);
  const [active, setActive] = useState<DocEntry | null>(null);
  const [markdown, setMarkdown] = useState<string | null>(null);
  const [loadingDoc, setLoadingDoc] = useState(false);

  const groups = useMemo(() => groupByOrg(catalog), [catalog]);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const entries = await buildCatalog();
      if (cancelled) return;
      setCatalog(entries);
      setLoadingCatalog(false);
      const hash = readHash();
      const initial =
        (hash ? entries.find((e) => e.path === hash || e.id === hash) : null) ??
        entries.find((e) => e.handAuthored) ??
        entries[0] ??
        null;
      setActive(initial);
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    const onHash = () => {
      const hash = readHash();
      if (!hash) return;
      const next = catalog.find((e) => e.path === hash || e.id === hash);
      if (next) setActive(next);
    };
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, [catalog]);

  useEffect(() => {
    if (!active) {
      setMarkdown(null);
      return;
    }
    let cancelled = false;
    setLoadingDoc(true);
    (async () => {
      const text = await loadMarkdown(active.path);
      if (cancelled) return;
      setMarkdown(text);
      setLoadingDoc(false);
    })();
    return () => {
      cancelled = true;
    };
  }, [active]);

  const select = (entry: DocEntry) => {
    setActive(entry);
    setMenuOpen(false);
    window.location.hash = encodeURIComponent(entry.path);
  };

  return (
    <div className="app-shell">
      <Sidebar
        groups={groups}
        activeId={active?.id ?? null}
        query={query}
        onQueryChange={setQuery}
        onSelect={select}
        open={menuOpen}
        onToggle={() => setMenuOpen(false)}
      />

      <div className="main">
        <header className="topbar">
          <button
            type="button"
            className="menu-btn"
            onClick={() => setMenuOpen(true)}
            aria-label="Open navigation"
          >
            Menu
          </button>
          <div className="topbar-copy">
            <p className="eyebrow">{active?.org ?? "—"}</p>
            <h2>{active?.title ?? (loadingCatalog ? "Loading…" : "Select a repository")}</h2>
          </div>
          <p className="doc-count">{catalog.length} docs</p>
        </header>

        <main className="content">
          {loadingCatalog && <p className="empty">Loading catalog…</p>}
          {!loadingCatalog && !active && <p className="empty">No architecture documents found.</p>}
          {active && loadingDoc && <p className="empty">Loading document…</p>}
          {active && !loadingDoc && !markdown && (
            <p className="empty">Could not load markdown for {active.path}.</p>
          )}
          {active && !loadingDoc && markdown && <MarkdownView markdown={markdown} />}
        </main>
      </div>

      {menuOpen ? (
        <button type="button" className="backdrop" onClick={() => setMenuOpen(false)} />
      ) : null}
    </div>
  );
}

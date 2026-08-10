import type { DocEntry } from "../lib/catalog";

type Props = {
  groups: Map<string, DocEntry[]>;
  activeId: string | null;
  query: string;
  onQueryChange: (value: string) => void;
  onSelect: (entry: DocEntry) => void;
  open: boolean;
  onToggle: () => void;
};

export function Sidebar({
  groups,
  activeId,
  query,
  onQueryChange,
  onSelect,
  open,
  onToggle,
}: Props) {
  const q = query.trim().toLowerCase();

  return (
    <aside className={`sidebar ${open ? "is-open" : ""}`}>
      <div className="sidebar-header">
        <div>
          <p className="eyebrow">Project repos</p>
          <h1>Architecture</h1>
        </div>
        <button type="button" className="sidebar-close" onClick={onToggle} aria-label="Close menu">
          ×
        </button>
      </div>

      <label className="search">
        <span className="sr-only">Search repositories</span>
        <input
          type="search"
          placeholder="Search repos…"
          value={query}
          onChange={(e) => onQueryChange(e.target.value)}
        />
      </label>

      <nav className="nav-groups">
        {[...groups.entries()].map(([org, entries]) => {
          const filtered = entries.filter((e) => {
            if (!q) return true;
            return (
              e.title.toLowerCase().includes(q) ||
              e.org.toLowerCase().includes(q) ||
              e.description.toLowerCase().includes(q)
            );
          });
          if (filtered.length === 0) return null;
          return (
            <section key={org} className="nav-group">
              <h2>{org}</h2>
              <ul>
                {filtered.map((entry) => (
                  <li key={entry.id}>
                    <button
                      type="button"
                      className={entry.id === activeId ? "is-active" : ""}
                      onClick={() => onSelect(entry)}
                    >
                      <span className="nav-title">
                        {entry.title}
                        {entry.handAuthored ? <em>hand</em> : null}
                      </span>
                      {entry.description ? (
                        <span className="nav-desc">{entry.description}</span>
                      ) : null}
                    </button>
                  </li>
                ))}
              </ul>
            </section>
          );
        })}
      </nav>
    </aside>
  );
}

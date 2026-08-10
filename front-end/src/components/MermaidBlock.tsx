import { useEffect, useId, useRef, useState } from "react";
import Panzoom, { type PanzoomObject } from "@panzoom/panzoom";
import { renderMermaidSvg } from "../lib/mermaid";

type Props = {
  code: string;
};

export function MermaidBlock({ code }: Props) {
  const hostRef = useRef<HTMLDivElement>(null);
  const viewportRef = useRef<HTMLDivElement>(null);
  const panzoomRef = useRef<PanzoomObject | null>(null);
  const reactId = useId().replace(/:/g, "");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(true);

  useEffect(() => {
    let cancelled = false;
    const host = hostRef.current;
    const viewport = viewportRef.current;
    if (!host || !viewport) return;

    setBusy(true);
    setError(null);
    panzoomRef.current?.destroy();
    panzoomRef.current = null;
    host.innerHTML = "";

    (async () => {
      try {
        const svg = await renderMermaidSvg(code);
        if (cancelled) return;
        host.innerHTML = svg;
        const svgEl = host.querySelector("svg");
        if (svgEl) {
          svgEl.style.maxWidth = "none";
          svgEl.style.height = "auto";
          svgEl.removeAttribute("width");
          // Keep height attribute if present for aspect; ensure readable size
          svgEl.style.minWidth = "640px";
        }

        const pz = Panzoom(host, {
          maxScale: 8,
          minScale: 0.15,
          cursor: "grab",
          canvas: true,
        });
        panzoomRef.current = pz;
        viewport.addEventListener("wheel", pz.zoomWithWheel, { passive: false });
        // Fit roughly after layout
        requestAnimationFrame(() => {
          pz.zoom(0.85, { animate: false });
          pz.pan(0, 0, { animate: false });
        });
        setBusy(false);
      } catch (err) {
        if (cancelled) return;
        setError(err instanceof Error ? err.message : String(err));
        setBusy(false);
      }
    })();

    return () => {
      cancelled = true;
      const pz = panzoomRef.current;
      if (pz && viewport) {
        viewport.removeEventListener("wheel", pz.zoomWithWheel);
        pz.destroy();
      }
      panzoomRef.current = null;
    };
  }, [code]);

  const zoomBy = (factor: number) => {
    panzoomRef.current?.zoom(panzoomRef.current.getScale() * factor, { animate: true });
  };

  const resetView = () => {
    const pz = panzoomRef.current;
    if (!pz) return;
    pz.reset({ animate: true });
    pz.zoom(0.85, { animate: true });
  };

  return (
    <figure className="mermaid-figure" aria-labelledby={`${reactId}-label`}>
      <div className="mermaid-toolbar">
        <span id={`${reactId}-label`} className="mermaid-label">
          Mermaid diagram
        </span>
        <div className="mermaid-actions">
          <button type="button" onClick={() => zoomBy(1.2)} title="Zoom in">
            +
          </button>
          <button type="button" onClick={() => zoomBy(1 / 1.2)} title="Zoom out">
            −
          </button>
          <button type="button" onClick={resetView} title="Reset view">
            Reset
          </button>
        </div>
      </div>
      {busy && <div className="mermaid-status">Rendering diagram…</div>}
      {error && (
        <div className="mermaid-error">
          <p>Could not render diagram.</p>
          <pre>{error}</pre>
          <details>
            <summary>Source</summary>
            <pre>{code}</pre>
          </details>
        </div>
      )}
      <div className="mermaid-viewport" ref={viewportRef}>
        <div className="mermaid-canvas" ref={hostRef} />
      </div>
      <figcaption className="mermaid-hint">Scroll to zoom · drag to pan</figcaption>
    </figure>
  );
}

import type { Mermaid } from "mermaid";

let mermaidPromise: Promise<Mermaid> | null = null;
let initialized = false;

async function getMermaid(): Promise<Mermaid> {
  if (!mermaidPromise) {
    mermaidPromise = import("mermaid").then((m) => m.default);
  }
  const mermaid = await mermaidPromise;
  if (!initialized) {
    mermaid.initialize({
      startOnLoad: false,
      maxTextSize: 200_000,
      maxEdges: 5_000,
      securityLevel: "strict",
      theme: "base",
      themeVariables: {
        fontFamily: '"IBM Plex Mono", ui-monospace, monospace',
        fontSize: "14px",
        primaryColor: "#e8f0ea",
        primaryTextColor: "#14201a",
        primaryBorderColor: "#2f5d4a",
        secondaryColor: "#f3efe6",
        tertiaryColor: "#f7f4ee",
        lineColor: "#3d4f45",
        textColor: "#14201a",
        mainBkg: "#e8f0ea",
        nodeBorder: "#2f5d4a",
        clusterBkg: "#f7f4ee",
        clusterBorder: "#8aa193",
        titleColor: "#14201a",
        edgeLabelBackground: "#f7f4ee",
      },
      flowchart: {
        htmlLabels: true,
        curve: "basis",
        useMaxWidth: false,
        wrappingWidth: 220,
        nodeSpacing: 36,
        rankSpacing: 48,
        padding: 16,
      },
      sequence: {
        useMaxWidth: false,
      },
      er: {
        useMaxWidth: false,
      },
    });
    initialized = true;
  }
  return mermaid;
}

let renderSeq = 0;

export async function renderMermaidSvg(code: string): Promise<string> {
  const api = await getMermaid();
  const id = `mermaid-diagram-${++renderSeq}`;
  const { svg } = await api.render(id, code.trim());
  return svg;
}

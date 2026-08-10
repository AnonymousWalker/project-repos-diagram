import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { Components } from "react-markdown";
import { MermaidBlock } from "./MermaidBlock";

type Props = {
  markdown: string;
};

function isMermaid(className?: string): boolean {
  if (!className) return false;
  return className.split(/\s+/).includes("language-mermaid");
}

const components: Components = {
  code({ className, children, ...props }) {
    const text = String(children).replace(/\n$/, "");
    // fenced blocks are not inline when they contain newlines / language class
    const inline = !className && !String(children).includes("\n");
    if (!inline && isMermaid(className)) {
      return <MermaidBlock code={text} />;
    }
    if (inline) {
      return (
        <code className={className} {...props}>
          {children}
        </code>
      );
    }
    return (
      <pre className="code-block">
        <code className={className} {...props}>
          {children}
        </code>
      </pre>
    );
  },
  a({ href, children, ...props }) {
    const external = href?.startsWith("http");
    return (
      <a href={href} {...props} {...(external ? { target: "_blank", rel: "noreferrer" } : {})}>
        {children}
      </a>
    );
  },
};

export function MarkdownView({ markdown }: Props) {
  return (
    <article className="markdown-body">
      <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
        {markdown}
      </ReactMarkdown>
    </article>
  );
}

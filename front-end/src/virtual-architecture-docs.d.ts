declare module "virtual:architecture-docs" {
  export type DocEntry = {
    id: string;
    title: string;
    org: string;
    path: string;
    description: string;
    handAuthored: boolean;
  };

  export const catalog: DocEntry[];
  export const loaders: Record<string, () => Promise<string>>;
  export function loadMarkdown(path: string): Promise<string | null>;
}

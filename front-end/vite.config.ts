import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { architectureDocsPlugin } from "./vite.architecture-plugin";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "..");

export default defineConfig({
  plugins: [react(), architectureDocsPlugin(repoRoot)],
  server: {
    port: 5173,
    fs: {
      allow: [repoRoot, __dirname],
    },
  },
  resolve: {
    alias: {
      "@content": repoRoot,
    },
  },
  base: "./",
});

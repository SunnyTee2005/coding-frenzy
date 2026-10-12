import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

// Tauri 開發模式固定使用 1420 埠（見 src-tauri/tauri.conf.json 的 devUrl）
export default defineConfig({
  plugins: [react()],
  clearScreen: false,
  server: {
    port: 1420,
    strictPort: true,
    watch: { ignored: ['**/src-tauri/**'] },
  },
  test: {
    environment: 'node',
  },
})

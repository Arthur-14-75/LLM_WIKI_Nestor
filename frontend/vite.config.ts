import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // Équivaut à 0.0.0.0
    port: 5173,
    watch: {
      usePolling: true, // Indispensable pour que Docker détecte tes modifs de fichiers sous Windows/macOS
    },
  },
})

import { defineConfig } from 'playwright/test';
export default defineConfig({
  testDir: './tests/browser',
  timeout: 120_000,
  use: {
    baseURL: 'http://127.0.0.1:8765', browserName: 'chromium',
    launchOptions: process.env.MAXIM_BROWSER_PATH ? { executablePath: process.env.MAXIM_BROWSER_PATH } : {},
  },
  webServer: { command: 'python -m http.server 8765 --bind 127.0.0.1 --directory site', url: 'http://127.0.0.1:8765/MAXIM/explore/', reuseExistingServer: !process.env.CI },
});

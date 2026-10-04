import { test, expect } from 'playwright/test';

test('real WASM searches guides under a project prefix', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const wasm = page.waitForResponse(response => response.url().endsWith('.wasm'));
  await page.goto('/MAXIM/explore/?q=rust%20ownership');
  expect((await wasm).status()).toBe(200);
  await expect(page.locator('#submit')).toBeEnabled({ timeout: 90_000 });
  await expect(page.locator('.result').first()).toBeVisible();
  await expect(page.locator('#status')).toContainText('entries');
  const target = await page.locator('.result h3 a').first().getAttribute('href');
  expect(new URL(target).pathname).toMatch(/^\/MAXIM\//);
  const response = await page.request.get(target);
  expect(response.ok()).toBeTruthy();
  await page.locator('#section').selectOption('languages');
  await expect(page.locator('.result .module').first()).toHaveText('languages');
  await page.locator('#query').fill('zzzznomatchingentryzzzz');
  await page.locator('#query').press('Enter');
  await expect(page.locator('#status')).toContainText('No matches');
  await expect(page.locator('.result')).toHaveCount(0);
  await page.locator('#query').fill(Array.from({ length: 17 }, (_, i) => `word${i}`).join(' '));
  await page.locator('#query').press('Enter');
  await expect(page.locator('#status')).toContainText('Use up to 16');
  await page.locator('#query').fill('');
  await page.locator('#query').press('Enter');
  await expect(page.locator('#status')).toContainText('Choose a starting point');
  expect(errors).toEqual([]);
});

test('mobile search is usable and has no horizontal overflow', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/MAXIM/explore/');
  await expect(page.locator('#submit')).toBeEnabled({ timeout: 90_000 });
  await page.getByRole('button', { name: 'Entropy', exact: true }).click();
  await expect(page.locator('.result').first()).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBeTruthy();
});

test('failed index download offers a readable recovery route', async ({ page }) => {
  await page.route('**/explore/index.json.gz', route => route.fulfill({ status: 503, body: 'unavailable' }));
  await page.goto('/MAXIM/explore/');
  await expect(page.locator('#status')).toContainText('Reload to retry');
  await expect(page.getByRole('link', { name: 'Read the library' })).toBeVisible();
});

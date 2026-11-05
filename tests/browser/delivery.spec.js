import { test, expect } from 'playwright/test';
import { createHash } from 'node:crypto';
import fs from 'node:fs/promises';

test('real Rust search and original font families work with all external requests blocked', async ({page, baseURL}) => {
  const outside = [];
  await page.route('**/*', route => {
    const url = new URL(route.request().url());
    if (url.origin !== new URL(baseURL).origin) { outside.push(url.href); return route.abort(); }
    return route.continue();
  });
  await page.goto('/MAXIM/explore/?q=rust%20ownership');
  await expect(page.locator('.result').first()).toBeVisible({timeout:90_000});
  const families = await page.evaluate(async () => {
    const rows = [];
    for (const family of ['DM Sans','Libre Caslon Display','EB Garamond','JetBrains Mono']) {
      const fonts = await document.fonts.load(`16px "${family}"`, 'Rust ownership');
      rows.push({family, count:fonts.length, loaded:fonts.every(font => font.status==='loaded')});
    }
    return rows;
  });
  expect(families.every(row => row.count > 0 && row.loaded)).toBeTruthy();
  const target = await page.locator('.result h3 a').first().getAttribute('href');
  await page.goto(target);
  await page.evaluate(() => document.fonts.ready);
  expect(await page.locator('body').evaluate(el => getComputedStyle(el).fontFamily)).toContain('EB Garamond');
  expect(outside).toEqual([]);
});

test('complete commit-bound source downloads while WASM is unavailable', async ({page}) => {
  await page.route('**/*.wasm', route => route.fulfill({status:503,body:'unavailable'}));
  await page.goto('/MAXIM/explore/');
  await expect(page.locator('#retry')).toBeVisible();
  const response = await page.request.get('/MAXIM/explore/BUILD-MANIFEST.json');
  expect(response.ok()).toBeTruthy(); const manifest = await response.json();
  await expect(page.locator('#source-revision')).toHaveText(manifest.source_commit.slice(0,12));
  await expect(page.locator('#index-revision')).toHaveAttribute('title',manifest.index.raw_sha256);
  const pending = page.waitForEvent('download');
  await page.getByRole('link',{name:'Download source',exact:true}).click();
  const download = await pending; expect(await download.failure()).toBeNull();
  const bytes = await fs.readFile(await download.path());
  expect(bytes.length).toBe(manifest.source.bytes);
  expect(createHash('sha256').update(bytes).digest('hex')).toBe(manifest.source.sha256);
  for (const name of ['Download adapter','Download index','Verification tools','Build receipt','Licenses','Rust dependency notices','Python dependency notices','Rust library notices','Font notices','Source manifest']) {
    const link = page.getByRole('link',{name,exact:true}); await expect(link).toBeVisible();
    const href = await link.getAttribute('href'); const result = await page.request.get(new URL(href,page.url()).href);
    expect(result.ok(),name).toBeTruthy();
  }
});

test('revision, source and notices remain discoverable without JavaScript', async ({browser,baseURL}) => {
  const context = await browser.newContext({javaScriptEnabled:false,baseURL});
  try {
    const page = await context.newPage(); await page.goto('/MAXIM/explore/');
    await expect(page.getByText('Enable JavaScript to search',{exact:false})).toBeVisible();
    const revision = await page.locator('#source-revision').textContent(); expect(revision).toMatch(/^[0-9a-f]{12}$/);
    await expect(page.getByRole('link',{name:'Download source',exact:true})).toHaveAttribute('href',/maxim-source-[0-9a-f]{40}\.zip$/);
    await expect(page.getByRole('link',{name:'Font notices',exact:true})).toBeVisible();
  } finally { await context.close(); }
});

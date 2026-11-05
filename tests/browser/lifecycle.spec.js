import { test, expect } from 'playwright/test';

// These are protocol/lifecycle fixtures in real browser Workers, not a second
// search engine. search.spec.js separately executes the complete Rust index.
const controlled = `
const pending = new Map();
self.onmessage = ({data}) => {
  if (data.type === 'init') self.postMessage({type:'ready',generation:data.generation,count:1,sections:['languages','philosophy']});
  if (data.type === 'search') pending.set(data.id,data);
  if (data.type === 'release') {
    const p=pending.get(data.id);
    self.postMessage({type:'results',generation:p.generation,id:p.id,total:1,ms:1,hits:[{entry:{title:p.query,text:p.query,url:'languages/01-RUST/',section:p.section||'languages'}}]});
  }
};`;

async function observeWorkers(page) {
  const closed = [];
  page.on('worker', worker => worker.on('close', () => closed.push(worker.url())));
  await page.addInitScript(() => {
    const NativeWorker = window.Worker;
    window.workerObservations = [];
    window.Worker = class extends NativeWorker {
      constructor(...args) {
        super(...args);
        this.observation = { worker: this, messages: [], terminated: false };
        window.workerObservations.push(this.observation);
      }
      postMessage(message, ...rest) {
        this.observation.messages.push(message);
        this.observation.handler = this.onmessage;
        return super.postMessage(message, ...rest);
      }
      terminate() { this.observation.terminated = true; return super.terminate(); }
    };
  });
  return closed;
}
async function fixture(page, body = controlled) {
  await page.route('**/explore/worker.js', route => route.fulfill({ contentType: 'text/javascript', body }));
}
async function lastSearch(page, worker = 0) {
  await expect.poll(() => page.evaluate(i => window.workerObservations[i]?.messages.filter(m => m.type === 'search').length || 0, worker)).toBeGreaterThan(0);
  return page.evaluate(i => window.workerObservations[i].messages.filter(m => m.type === 'search').at(-1), worker);
}
async function release(page, id, worker = 0) {
  await page.evaluate(({id, worker}) => window.workerObservations[worker].worker.postMessage({type:'release',id}), {id,worker});
}
async function stopped(page, closed, message) {
  await expect(page.locator('#status')).toContainText(message);
  await expect(page.locator('#retry')).toBeVisible();
  await expect(page.locator('#submit')).toBeDisabled();
  await expect(page.locator('.result')).toHaveCount(0);
  await expect.poll(() => page.evaluate(() => window.workerObservations[0].terminated)).toBe(true);
  await expect.poll(() => closed.length).toBe(1);
  await expect(page.getByRole('link', {name:'Download WASM'})).toBeVisible();
  await expect(page.getByRole('link', {name:'Read the library'})).toBeVisible();
}

test('a failed actual index download retries successfully in a fresh worker', async ({page}) => {
  const closed = await observeWorkers(page);
  let attempts = 0;
  await page.route('**/explore/index.json.gz', route => ++attempts === 1 ? route.fulfill({status:503,body:'unavailable'}) : route.continue());
  await page.goto('/MAXIM/explore/?q=rust%20ownership&module=languages');
  await stopped(page, closed, 'Search could not load or run');
  await page.locator('#retry').click();
  await expect(page.locator('.result').first()).toBeVisible({timeout:90_000});
  await expect(page.locator('#section')).toHaveValue('languages');
  await expect(page.locator('#engine')).toContainText('42,242 entries');
  expect(attempts).toBe(2);
  expect(await page.evaluate(() => window.workerObservations.length)).toBe(2);
});

test('initialization deadline actually closes a stalled worker', async ({page}) => {
  const closed = await observeWorkers(page);
  await fixture(page, 'self.onmessage=()=>{};');
  await page.clock.install();
  await page.goto('/MAXIM/explore/');
  await expect.poll(() => page.evaluate(() => window.workerObservations[0]?.messages.length)).toBe(1);
  await page.clock.fastForward(120_001);
  await stopped(page, closed, 'took too long to load');
});

test('compute deadline actually terminates a blocked worker', async ({page}) => {
  const closed = await observeWorkers(page);
  await fixture(page, `self.onmessage=({data})=>{if(data.type==='init')self.postMessage({type:'ready',generation:data.generation,count:1,sections:[]});else while(true){}};`);
  await page.clock.install();
  await page.goto('/MAXIM/explore/?q=entropy');
  await lastSearch(page);
  await page.clock.fastForward(15_001);
  await stopped(page, closed, 'Search took too long');
});

test('stop during initialization preserves the draft and starts a new worker on retry', async ({page}) => {
  const closed = await observeWorkers(page);
  await fixture(page, 'self.onmessage=()=>{};');
  await page.goto('/MAXIM/explore/');
  await expect(page.locator('#stop')).toBeVisible();
  await page.locator('#query').fill('my next idea');
  await page.locator('#stop').click();
  await stopped(page, closed, 'Search was stopped');
  await page.unroute('**/explore/worker.js');
  await fixture(page);
  await page.locator('#retry').click();
  const next = await lastSearch(page, 1);
  expect(next.query).toBe('my next idea');
  await release(page, next.id, 1);
  await expect(page.locator('.result h3')).toHaveText('my next idea');
});

test('stop during computation clears results and closes the active worker', async ({page}) => {
  const closed = await observeWorkers(page); await fixture(page);
  await page.goto('/MAXIM/explore/?q=entropy');
  await lastSearch(page);
  await page.locator('#stop').click();
  await stopped(page, closed, 'Search was stopped');
  await expect(page.locator('#query')).toHaveValue('entropy');
});

test('edits clear results immediately and ignore an older in-flight reply', async ({page}) => {
  await observeWorkers(page); await fixture(page);
  await page.goto('/MAXIM/explore/?q=first');
  const first = await lastSearch(page); await release(page, first.id);
  await expect(page.locator('.result h3')).toHaveText('first');
  await page.locator('#query').fill('second');
  await expect(page.locator('.result')).toHaveCount(0);
  await page.locator('#query').press('Enter');
  const second = await lastSearch(page);
  expect(second.query).toBe('second');
  await page.locator('#query').fill('latest');
  await release(page, second.id);
  await expect(page.locator('.result')).toHaveCount(0);
  await expect.poll(async () => (await lastSearch(page)).query).toBe('latest');
  const latest = await lastSearch(page); await release(page, latest.id);
  await expect(page.locator('.result h3')).toHaveText('latest');
  await page.locator('#query').fill('');
  await expect(page.locator('.result')).toHaveCount(0);
  await release(page, latest.id);
  await expect(page.locator('.result')).toHaveCount(0);
  await expect(page.locator('#status')).toContainText('Choose a starting point');
});

test('a module change queues only the latest request behind active computation', async ({page}) => {
  await observeWorkers(page); await fixture(page);
  await page.goto('/MAXIM/explore/?q=idea');
  const first = await lastSearch(page);
  await page.locator('#section').selectOption('philosophy');
  await page.locator('#section').selectOption('languages');
  await release(page, first.id);
  await expect.poll(async () => (await lastSearch(page)).section).toBe('languages');
  const latest = await lastSearch(page); await release(page, latest.id);
  await expect(page.locator('.result .module')).toHaveText('languages');
  expect(await page.evaluate(() => window.workerObservations[0].messages.filter(m => m.type==='search').length)).toBe(2);
});

test('captured previous-generation replies cannot affect a restarted session', async ({page}) => {
  await observeWorkers(page); await fixture(page);
  await page.goto('/MAXIM/explore/?q=idea');
  const first = await lastSearch(page);
  await page.locator('#stop').click(); await page.locator('#retry').click();
  const current = await lastSearch(page, 1);
  await page.evaluate(({first,current}) => {
    const old = window.workerObservations[0].handler;
    old({data:{type:'ready',generation:first.generation,count:999,sections:['forged']}});
    old({data:{type:'error',generation:first.generation}});
    old({data:{type:'results',generation:current.generation,id:current.id,total:999,ms:0,hits:[]}});
  }, {first,current});
  await expect(page.locator('#engine')).toContainText('1 entries');
  await expect(page.locator('#retry')).toBeHidden();
  await release(page, current.id, 1);
  await expect(page.locator('.result h3')).toHaveText('idea');
});

test('unreadable worker messages retire the session with usable navigation', async ({page}) => {
  const closed = await observeWorkers(page); await fixture(page);
  await page.goto('/MAXIM/explore/?q=idea'); await lastSearch(page);
  await page.evaluate(() => window.workerObservations[0].worker.dispatchEvent(new MessageEvent('messageerror')));
  await stopped(page, closed, 'unreadable response');
});

test('worker construction failure retains recovery and download links', async ({page}) => {
  await page.addInitScript(() => { window.Worker = class { constructor() { throw new Error('unsupported'); } }; });
  await page.goto('/MAXIM/explore/');
  await expect(page.locator('#status')).toContainText('Search could not load');
  await expect(page.locator('#retry')).toBeVisible();
  await expect(page.getByRole('link', {name:'Download WASM'})).toBeVisible();
  await expect(page.getByRole('link', {name:'Download source'})).toBeVisible();
});

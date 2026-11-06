const $ = (selector) => document.querySelector(selector);
const query = $('#query'), section = $('#section'), status = $('#status'), results = $('#results');
// Initialization includes the complete 35 MB compressed index, not just WASM.
const INITIALIZATION_TIMEOUT_MS = 120_000, SEARCH_TIMEOUT_MS = 15_000;
let worker, ready = false, request = 0, generation = 0, limit = 20, timer;
let bootTimer, computeTimer, activeRequest = null, pending = null;
const params = new URLSearchParams(location.search);
query.value = (params.get('q') || '').slice(0, 512);

function clearResults() {
  results.replaceChildren();
  $('#more').hidden = true;
}
function retire() {
  generation++;
  request++;
  clearTimeout(timer); clearTimeout(bootTimer); clearTimeout(computeTimer);
  pending = null; activeRequest = null;
  if (worker) {
    worker.onmessage = null; worker.onerror = null;
    worker.terminate(); worker = null;
  }
  ready = false;
}
function fail(message) {
  retire();
  $('#submit').disabled = true;
  section.disabled = true;
  clearResults();
  $('#stop').hidden = true; $('#retry').hidden = false;
  $('#results-title').textContent = 'Choose another path';
  status.textContent = message + ' Retry search, or browse the library above.';
}
function invalidate() {
  request++; pending = null;
  clearResults();
}
function dispatch() {
  if (!ready || activeRequest !== null || !pending) return;
  const message = pending; pending = null; activeRequest = message.id;
  $('#stop').hidden = false;
  computeTimer = setTimeout(() => fail('Search took too long and was stopped.'), SEARCH_TIMEOUT_MS);
  try { worker.postMessage(message); }
  catch { fail('Search could not run.'); }
}
function search() {
  clearTimeout(timer);
  invalidate();
  if (!ready) return;
  const q = query.value.trim();
  const next = new URL(location.href);
  q ? next.searchParams.set('q', q) : next.searchParams.delete('q');
  section.value ? next.searchParams.set('module', section.value) : next.searchParams.delete('module');
  history.replaceState(null, '', next);
  if (!q) {
    $('#results-title').textContent = 'A world of connections';
    status.textContent = 'Choose a starting point above, or search for an idea.';
    return;
  }
  const words = new Set(q.toLowerCase().match(/[\p{L}\p{N}]+/gu) || []);
  if (new TextEncoder().encode(q).length > 512 || words.size > 16) {
    status.textContent = 'Use up to 16 different words and 512 UTF-8 bytes.';
    return;
  }
  status.textContent = 'Searching…';
  pending = { type: 'search', query: q, section: section.value, limit, id: request, generation };
  dispatch();
}
function highlight(parent, text) {
  // Text nodes only: guide content and queries never become HTML.
  const words = [...new Set(query.value.toLocaleLowerCase().match(/[\p{L}\p{N}]+/gu) || [])];
  const expression = words.length ? new RegExp(`(${words.join('|')})`, 'giu') : null;
  for (const chunk of expression ? text.split(expression) : [text]) {
    if (words.includes(chunk.toLocaleLowerCase())) {
      const mark = document.createElement('mark'); mark.textContent = chunk; parent.append(mark);
    } else parent.append(document.createTextNode(chunk));
  }
}
function excerpt(text) {
  const word = query.value.toLocaleLowerCase().match(/[\p{L}\p{N}]+/u)?.[0];
  const position = word ? text.toLocaleLowerCase().indexOf(word) : 0;
  const start = Math.max(0, position - 70), end = Math.min(text.length, start + 300);
  return `${start ? '…' : ''}${text.slice(start, end)}${end < text.length ? '…' : ''}`;
}
function render(data) {
  if (data.id !== request) return;
  results.replaceChildren();
  $('#results-title').textContent = data.total ? 'Your next discovery' : 'Try another path';
  status.textContent = data.total ? `${data.total.toLocaleString()} entries · ${data.ms.toFixed(1)} ms · showing ${data.hits.length}` : 'No matches. Try fewer words or choose all modules.';
  const base = new URL('../', location.href);
  for (const { entry } of data.hits) {
    const url = new URL(entry.url, base);
    if (url.origin !== base.origin || !url.pathname.startsWith(base.pathname)) continue;
    const article = document.createElement('article'); article.className = 'result';
    const module = document.createElement('span'); module.className = 'module'; module.textContent = entry.section.replaceAll('-', ' ');
    const heading = document.createElement('h3'), link = document.createElement('a'); link.href = url.href;
    highlight(link, entry.title); heading.append(link);
    const text = document.createElement('p'); highlight(text, excerpt(entry.text));
    const path = document.createElement('a'); path.className = 'path'; path.href = url.href; path.textContent = `${entry.url} ↗`;
    article.append(module, heading, text, path); results.append(article);
  }
  $('#more').hidden = data.hits.length >= data.total || limit >= 100;
}
$('#search-form').addEventListener('submit', (event) => { event.preventDefault(); clearTimeout(timer); limit = 20; search(); });
query.addEventListener('input', () => {
  clearTimeout(timer); invalidate(); limit = 20;
  if (ready) status.textContent = 'Waiting for your search…';
  timer = setTimeout(search, 180);
});
section.addEventListener('change', () => { limit = 20; search(); });
$('#more').addEventListener('click', () => { limit += 20; search(); });
document.querySelectorAll('[data-query]').forEach((button) => button.addEventListener('click', () => { query.value = button.dataset.query; limit = 20; search(); query.focus(); }));
function start() {
  retire(); clearResults();
  const epoch = generation;
  $('#submit').disabled = true; section.disabled = true;
  $('#stop').hidden = false; $('#retry').hidden = true;
  status.textContent = 'Loading the search library (about 35 MB)…';
  $('#results-title').textContent = 'A world of connections';
  try {
    worker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
    bootTimer = setTimeout(() => fail('The search library took too long to load and was stopped.'), INITIALIZATION_TIMEOUT_MS);
    worker.onerror = (event) => {
      if (epoch !== generation) return;
      event.preventDefault(); fail('Search could not load or run.');
    };
    worker.addEventListener('messageerror', () => { if (epoch === generation) fail('Search returned an unreadable response.'); });
    worker.onmessage = ({ data }) => {
      if (epoch !== generation || data.generation !== epoch) return;
      if (data.type === 'ready' && !ready) {
        clearTimeout(bootTimer); ready = true;
        section.replaceChildren(new Option('All modules', ''));
        for (const name of data.sections) section.add(new Option(name.replaceAll('-', ' '), name));
        const selected = new URLSearchParams(location.search).get('module');
        if (data.sections.includes(selected)) section.value = selected;
        $('#submit').disabled = false; section.disabled = false; $('#stop').hidden = true;
        $('#engine').textContent = `${data.count.toLocaleString()} entries · Rust + WebAssembly · searches stay on your device`;
        search();
      } else if (data.type === 'results' && data.id === activeRequest) {
        clearTimeout(computeTimer); activeRequest = null; $('#stop').hidden = true;
        render(data); dispatch();
      } else if (data.type === 'error') fail('Search could not load or run.');
    };
    worker.postMessage({ type: 'init', generation: epoch });
  } catch { fail('Search could not load.'); }
}
$('#stop').addEventListener('click', () => fail('Search was stopped.'));
$('#retry').addEventListener('click', start);
window.addEventListener('pagehide', retire);
window.addEventListener('pageshow', event => { if (event.persisted) start(); });
start();

const $ = (selector) => document.querySelector(selector);
const query = $('#query'), section = $('#section'), status = $('#status'), results = $('#results');
let worker, ready = false, request = 0, limit = 20, timer;
const params = new URLSearchParams(location.search);
query.value = (params.get('q') || '').slice(0, 512);

function fail() {
  ready = false;
  $('#submit').disabled = true;
  section.disabled = true;
  results.replaceChildren();
  $('#more').hidden = true;
  status.textContent = 'Search could not load. Reload to retry, or browse the library above.';
}
function search() {
  if (!ready) return;
  const q = query.value.trim();
  const next = new URL(location.href);
  q ? next.searchParams.set('q', q) : next.searchParams.delete('q');
  section.value ? next.searchParams.set('module', section.value) : next.searchParams.delete('module');
  history.replaceState(null, '', next);
  request++;
  if (!q) {
    results.replaceChildren(); $('#more').hidden = true;
    $('#results-title').textContent = 'A world of connections';
    status.textContent = 'Choose a starting point above, or search for an idea.';
    return;
  }
  const words = new Set(q.toLowerCase().match(/[\p{L}\p{N}]+/gu) || []);
  if (new TextEncoder().encode(q).length > 512 || words.size > 16) {
    results.replaceChildren(); $('#more').hidden = true;
    status.textContent = 'Use up to 16 different words and 512 UTF-8 bytes.';
    return;
  }
  status.textContent = 'Searching…';
  worker.postMessage({ type: 'search', query: q, section: section.value, limit, id: request });
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
query.addEventListener('input', () => { clearTimeout(timer); request++; limit = 20; timer = setTimeout(search, 180); });
section.addEventListener('change', () => { limit = 20; search(); });
$('#more').addEventListener('click', () => { limit += 20; search(); });
document.querySelectorAll('[data-query]').forEach((button) => button.addEventListener('click', () => { query.value = button.dataset.query; limit = 20; search(); query.focus(); }));
try {
  worker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
  worker.onerror = fail;
  worker.onmessage = ({ data }) => {
    if (data.type === 'ready') {
      ready = true;
      for (const name of data.sections) { const option = new Option(name.replaceAll('-', ' '), name); section.add(option); }
      if (data.sections.includes(params.get('module'))) section.value = params.get('module');
      $('#submit').disabled = false; section.disabled = false;
      $('#engine').textContent = `${data.count.toLocaleString()} entries · Rust + WebAssembly · searches stay on your device`;
      search();
    } else if (data.type === 'results') render(data);
    else if (data.type === 'error') fail();
  };
  worker.postMessage({ type: 'init' });
} catch { fail(); }

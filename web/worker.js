import init, { SearchIndex } from './pkg/maxim_search.js';
let index, generation;
self.onmessage = async ({ data }) => {
  try {
    if (data.type === 'init') {
      generation = data.generation;
      const start = performance.now();
      await init();
      const response = await fetch('./index.json.gz');
      if (!response.ok) throw new Error(`Index download failed (${response.status})`);
      const stream = response.body.pipeThrough(new DecompressionStream('gzip'));
      index = new SearchIndex(await new Response(stream).text());
      self.postMessage({ type: 'ready', generation, count: index.count(), sections: JSON.parse(index.sections()), ms: performance.now() - start });
    } else if (data.type === 'search' && index && data.generation === generation) {
      const start = performance.now();
      const result = JSON.parse(index.search(data.query, data.section, data.limit));
      self.postMessage({ type: 'results', generation, id: data.id, ...result, ms: performance.now() - start });
    }
  } catch (error) {
    self.postMessage({ type: 'error', generation, id: data.id, message: String(error) });
  }
};

//! A precomputed inverted index shared by native tools and WebAssembly.
//! Queries intersect sorted posting lists; they never scan the full corpus.
use serde::{Deserialize, Serialize};
use std::collections::{BTreeMap, BTreeSet};

const VERSION: u32 = 1;
const MAX_QUERY_TOKENS: usize = 16;
const MAX_RESULTS: usize = 100;

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Entry {
    pub title: String,
    pub url: String,
    pub section: String,
    pub text: String,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(from = "(usize, u32)", into = "(usize, u32)")]
struct Posting {
    doc: usize,
    weight: u32,
}

impl From<(usize, u32)> for Posting {
    fn from((doc, weight): (usize, u32)) -> Self {
        Self { doc, weight }
    }
}

impl From<Posting> for (usize, u32) {
    fn from(posting: Posting) -> Self {
        (posting.doc, posting.weight)
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct Index {
    version: u32,
    entries: Vec<Entry>,
    terms: BTreeMap<String, Vec<Posting>>,
}

#[derive(Debug, Serialize)]
pub struct Hit<'a> {
    pub entry: &'a Entry,
    pub score: f64,
}

#[derive(Debug, Serialize)]
pub struct Results<'a> {
    pub total: usize,
    pub hits: Vec<Hit<'a>>,
}

pub fn tokenize(text: &str) -> Vec<String> {
    text.split(|c: char| !c.is_alphanumeric())
        .filter(|s| !s.is_empty())
        .map(str::to_lowercase)
        .collect()
}

impl Index {
    /// Build deterministically in input order. Titles carry extra ranking weight.
    pub fn build(entries: Vec<Entry>) -> Self {
        let mut terms: BTreeMap<String, Vec<Posting>> = BTreeMap::new();
        for (doc, entry) in entries.iter().enumerate() {
            let mut counts: BTreeMap<String, usize> = BTreeMap::new();
            let body = tokenize(&entry.text);
            let length = body.len().max(1) as f64;
            for term in body {
                *counts.entry(term).or_default() += 1;
            }
            let titles: BTreeSet<_> = tokenize(&entry.title).into_iter().collect();
            for term in &titles {
                counts.entry(term.clone()).or_default();
            }
            for (term, count) in counts {
                let tf = count as f64;
                let title_boost = if titles.contains(&term) { 4.0 } else { 0.0 };
                let weight = title_boost + tf / (tf + 0.5 + length / 500.0);
                terms.entry(term).or_default().push(Posting {
                    doc,
                    weight: (weight * 1000.0).round() as u32,
                });
            }
        }
        let n = entries.len() as f64;
        for postings in terms.values_mut() {
            let idf = (1.0 + (n + 0.5) / (postings.len() as f64 + 0.5)).ln();
            for posting in postings {
                posting.weight = (f64::from(posting.weight) * idf).round() as u32;
            }
        }
        Self {
            version: VERSION,
            entries,
            terms,
        }
    }

    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string(self)
    }

    /// Validate schema and posting invariants before queries can dereference IDs.
    pub fn from_json(json: &str) -> Result<Self, String> {
        let index: Self = serde_json::from_str(json).map_err(|e| e.to_string())?;
        if index.version != VERSION {
            return Err("Unsupported search index version".into());
        }
        for postings in index.terms.values() {
            let mut previous = None;
            for p in postings {
                if p.doc >= index.entries.len() || previous.is_some_and(|id| id >= p.doc) {
                    return Err("Invalid search index posting".into());
                }
                previous = Some(p.doc);
            }
        }
        Ok(index)
    }

    pub fn len(&self) -> usize {
        self.entries.len()
    }
    pub fn is_empty(&self) -> bool {
        self.entries.is_empty()
    }
    pub fn sections(&self) -> Vec<&str> {
        self.entries
            .iter()
            .map(|e| e.section.as_str())
            .collect::<BTreeSet<_>>()
            .into_iter()
            .collect()
    }

    /// All distinct query words must match. No stemming, fuzzy or phrase syntax.
    /// Limit is clamped to 100; section is an exact optional module identifier.
    pub fn search(&self, query: &str, section: &str, limit: usize) -> Results<'_> {
        let empty = || Results {
            total: 0,
            hits: vec![],
        };
        if query.len() > 512 {
            return empty();
        }
        let tokens: BTreeSet<_> = tokenize(query).into_iter().collect();
        if tokens.is_empty() || tokens.len() > MAX_QUERY_TOKENS {
            return empty();
        }
        let mut lists = Vec::new();
        for token in &tokens {
            let Some(list) = self.terms.get(token) else {
                return empty();
            };
            lists.push(list);
        }
        lists.sort_by_key(|list| list.len());
        let mut hits = Vec::new();
        let mut total = 0;
        let limit = limit.min(MAX_RESULTS);
        for candidate in lists[0] {
            let entry = &self.entries[candidate.doc];
            if !section.is_empty() && entry.section != section {
                continue;
            }
            let mut score = f64::from(candidate.weight) / 1000.0;
            let mut matched = true;
            for list in &lists[1..] {
                match list.binary_search_by_key(&candidate.doc, |p| p.doc) {
                    Ok(i) => score += f64::from(list[i].weight) / 1000.0,
                    Err(_) => {
                        matched = false;
                        break;
                    }
                }
            }
            if matched {
                total += 1;
                if limit == 0 {
                    continue;
                }
                hits.push(Hit { entry, score });
                // Bounded top-k: at most 101 entries, independent of corpus size.
                hits.sort_unstable_by(|a, b| {
                    b.score
                        .total_cmp(&a.score)
                        .then_with(|| a.entry.url.cmp(&b.entry.url))
                });
                hits.truncate(limit);
            }
        }
        Results { total, hits }
    }
}

#[cfg(feature = "wasm")]
mod browser {
    use super::Index;
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen]
    pub struct SearchIndex {
        inner: Index,
    }

    #[wasm_bindgen]
    impl SearchIndex {
        #[wasm_bindgen(constructor)]
        pub fn new(json: &str) -> Result<SearchIndex, JsValue> {
            Ok(Self {
                inner: Index::from_json(json).map_err(|e| JsValue::from_str(&e))?,
            })
        }
        pub fn count(&self) -> usize {
            self.inner.len()
        }
        pub fn sections(&self) -> String {
            serde_json::to_string(&self.inner.sections()).expect("string serialization")
        }
        pub fn search(&self, query: &str, section: &str, limit: usize) -> String {
            serde_json::to_string(&self.inner.search(query, section, limit)).expect("finite scores")
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    fn entry(title: &str, text: &str, section: &str, url: &str) -> Entry {
        Entry {
            title: title.into(),
            text: text.into(),
            section: section.into(),
            url: url.into(),
        }
    }
    fn index() -> Index {
        Index::build(vec![
            entry(
                "Rust ownership",
                "Memory safety through ownership and borrowing",
                "computing",
                "computing/ownership/",
            ),
            entry(
                "Languages",
                "Rust and memory safety",
                "languages",
                "languages/rust/",
            ),
            entry(
                "Ocean currents",
                "Water circulation and climate",
                "earth",
                "earth/ocean/",
            ),
        ])
    }
    #[test]
    fn ranks_title_above_body() {
        let i = index();
        let r = i.search("rust", "", 10);
        assert_eq!(r.total, 2);
        assert_eq!(r.hits[0].entry.title, "Rust ownership");
    }
    #[test]
    fn intersects_and_deduplicates() {
        let i = index();
        assert_eq!(i.search("rust ownership", "", 10).total, 1);
        assert_eq!(i.search("rust ocean", "", 10).total, 0);
        assert_eq!(
            i.search("rust rust", "", 10).hits[0].score,
            i.search("rust", "", 10).hits[0].score
        );
    }
    #[test]
    fn filters_and_limits_without_losing_total() {
        let i = index();
        assert_eq!(i.search("rust", "languages", 10).total, 1);
        let r = i.search("rust", "", 1);
        assert_eq!(r.total, 2);
        assert_eq!(r.hits.len(), 1);
        assert_eq!(i.search("rust", "", 0).total, 2);
        assert!(i.search("rust", "", 0).hits.is_empty());
    }
    #[test]
    fn empty_unknown_and_unicode() {
        let i = index();
        for q in ["", "!?", "unknown", &"r".repeat(513)] {
            assert_eq!(i.search(q, "", 10).total, 0);
        }
        let i = Index::build(vec![entry("ÉCOLOGIE", "植物 écologie", "life", "life/")]);
        assert_eq!(i.search("Écologie", "", 10).total, 1);
        assert_eq!(i.search("植物", "", 10).total, 1);
    }
    #[test]
    fn roundtrip_and_reject_corruption() {
        let json = index().to_json().unwrap();
        assert_eq!(
            Index::from_json(&json)
                .unwrap()
                .search("rust", "", 10)
                .total,
            2
        );
        assert!(Index::from_json(&json.replace("\"version\":1", "\"version\":2")).is_err());
        let mut corrupted: serde_json::Value = serde_json::from_str(&json).unwrap();
        corrupted["terms"]["rust"][0][0] = 999.into();
        assert!(Index::from_json(&corrupted.to_string()).is_err());
        assert!(Index::from_json("{}").is_err());
    }

    #[test]
    fn top_k_is_bounded_and_ties_are_deterministic() {
        let entries = (0..150)
            .rev()
            .map(|i| entry("Same", "same", "test", &format!("test/{i:03}/")))
            .collect();
        let index = Index::build(entries);
        let result = index.search("same", "", 1000);
        assert_eq!(result.total, 150);
        assert_eq!(result.hits.len(), 100);
        assert_eq!(result.hits[0].entry.url, "test/000/");
        assert_eq!(result.hits[99].entry.url, "test/099/");
    }

    #[test]
    fn rejects_duplicate_postings_and_excess_query_terms() {
        let mut json: serde_json::Value =
            serde_json::from_str(&index().to_json().unwrap()).unwrap();
        json["terms"]["rust"][1][0] = 0.into();
        assert!(Index::from_json(&json.to_string()).is_err());
        let query = (0..17)
            .map(|i| format!("term{i}"))
            .collect::<Vec<_>>()
            .join(" ");
        assert_eq!(index().search(&query, "", 10).total, 0);
    }
}

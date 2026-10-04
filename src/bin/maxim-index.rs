use maxim_search::{Entry, Index};
use std::{env, error::Error, fs, time::Instant};

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<_> = env::args().collect();
    if args.len() != 3 {
        return Err("Usage: maxim-index <entries.json> <index.json>".into());
    }
    let start = Instant::now();
    let entries: Vec<Entry> = serde_json::from_str(&fs::read_to_string(&args[1])?)?;
    let index = Index::build(entries);
    let json = index.to_json()?;
    fs::write(&args[2], &json)?;
    eprintln!(
        "{} entries; {} bytes; built in {:?}",
        index.len(),
        json.len(),
        start.elapsed()
    );
    for query in ["rust ownership", "entropy", "climate", "decision"] {
        let start = Instant::now();
        let result = index.search(query, "", 20);
        eprintln!(
            "{query:?}: {} matches in {:?}",
            result.total,
            start.elapsed()
        );
    }
    Ok(())
}

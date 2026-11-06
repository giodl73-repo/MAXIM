//! Native observation seam over the original Index, not a second search policy.
use maxim_search::Index;
use serde::Deserialize;
use std::io::{self, BufRead};

#[derive(Deserialize)]
struct Query {
    query: String,
    section: String,
    limit: usize,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let path = std::env::args()
        .nth(1)
        .ok_or("Expected an index JSON path")?;
    let raw = std::fs::read_to_string(path)?;
    let index = match Index::from_json(&raw) {
        Ok(index) => index,
        Err(error) => {
            println!("{}", serde_json::json!({"ok": false, "error": error}));
            std::process::exit(2);
        }
    };
    println!(
        "{}",
        serde_json::json!({"ok": true, "count": index.len(), "sections_json": serde_json::to_string(&index.sections())?})
    );
    for line in io::stdin().lock().lines() {
        let query: Query = serde_json::from_str(&line?)?;
        let result =
            serde_json::to_string(&index.search(&query.query, &query.section, query.limit))?;
        println!("{}", serde_json::json!({"ok": true, "json": result}));
    }
    Ok(())
}

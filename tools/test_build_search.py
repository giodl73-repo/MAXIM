import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("build_search", Path(__file__).with_name("build-search.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SearchBuildTests(unittest.TestCase):
    def test_only_real_guide_urls_and_unique_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            page = site / "computing/01-PACKAGE/index.html"
            page.parent.mkdir(parents=True)
            page.write_text("<h2 id='test'>Test</h2>")
            guide = {"location": "computing/01-PACKAGE/#test", "title": "<b>Package</b>", "text": "<p>Rust &amp; tools</p>"}
            docs = [guide, guide] + [{**guide, "location": url} for url in ["context/private/", "README/", "https://example.com/01-GUIDE/", "../01-SECRET/", ".proof/01-GUIDE/"]]
            result = module.entries_from_docs(docs, site)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["text"], "Rust & tools")
            self.assertEqual(result[0]["section"], "computing")

    def test_missing_rendered_page_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                module.entries_from_docs([{"location": "computing/01-MISSING/", "title": "Missing", "text": ""}], Path(directory))

    def test_percent_encoded_guide_name(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            page = site / "fashion/02-PRÊT/index.html"
            page.parent.mkdir(parents=True)
            page.write_text("guide")
            url = "fashion/02-PR%C3%8AT/#ready"
            result = module.entries_from_docs([{"location": url, "title": "Prêt", "text": "Guide"}], site)
            self.assertEqual(result[0]["url"], url)


if __name__ == "__main__":
    unittest.main()

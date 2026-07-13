"""Citation network analyzer."""
import re; from pathlib import Path
from collections import Counter
class CitationAnalyzer:
    def analyze(self, path: Path) -> dict:
        all_refs = []; all_authors = []; years = []
        for f in list(path.rglob("*.md")) + list(path.rglob("*.txt")):
            try: c = f.read_text(errors="ignore")
            except: continue
            refs = re.findall(r"(?:doi:\s*)?(10\.\d{4,}/[^\s\)]+)", c)
            all_refs.extend(refs)
            authors = re.findall(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})", c)
            all_authors.extend(authors)
            yrs = re.findall(r"\b(19|20)\d{2}\b", c)
            years.extend([int(y) for y in yrs if 1900 <= int(y) <= 2030])
        return {
            "unique_dois": len(set(all_refs)),
            "top_authors": [{"name": n, "count": c} for n, c in Counter(all_authors).most_common(10)],
            "year_distribution": dict(Counter(years).most_common(10)),
            "total_references": len(all_refs),
        }

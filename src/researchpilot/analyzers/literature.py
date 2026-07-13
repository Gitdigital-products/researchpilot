"""Literature review analyzer."""
import re; from pathlib import Path
class LiteratureAnalyzer:
    def analyze(self, path: Path) -> dict:
        papers = []
        for f in list(path.rglob("*.md")) + list(path.rglob("*.txt")) + list(path.rglob("*.rst")):
            if ".venv" in str(f) or "node_modules" in str(f): continue
            try:
                c = f.read_text(errors="ignore")
                title_match = re.search(r"^#\s+(.+)$", c, re.M)
                title = title_match.group(1).strip() if title_match else f.stem
                abstract_match = re.search(r"(?:abstract|summary)[:\s]*(.{50,500})", c, re.I|re.S)
                abstract = abstract_match.group(1).strip()[:200] if abstract_match else ""
                keywords = re.findall(r"(?:keywords?|tags?)[:\s]*(.+)", c, re.I)
                refs = len(re.findall(r"\[\d+\]|et al\.", c))
                papers.append({"file": str(f), "title": title, "abstract": abstract, "keywords": [k.strip() for k in keywords[0].split(",")][:5] if keywords else [], "reference_count": refs})
            except: pass
        return {"papers": papers, "total": len(papers), "avg_references": sum(p["reference_count"] for p in papers) / max(len(papers), 1)}

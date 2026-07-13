"""Research finding extractor."""
import re; from pathlib import Path
class FindingExtractor:
    def extract(self, path: Path) -> dict:
        findings = []
        if path.is_file():
            findings.extend(self._extract_file(path))
        elif path.is_dir():
            for f in list(path.rglob("*.md")) + list(path.rglob("*.txt")):
                if ".venv" in str(f): continue
                findings.extend(self._extract_file(f))
        return {"findings": findings, "total": len(findings)}
    def _extract_file(self, path: Path) -> list:
        results = []
        try:
            c = path.read_text(errors="ignore")
            patterns = [
                (re.compile(r"(?:results?|finding|conclusion)[:\s]+(.{20,300})", re.I), "result"),
                (re.compile(r"(?:we (?:show|demonstrate|prove|find|observe|discover))\s+(.{20,300})", re.I), "contribution"),
                (re.compile(r"(?:accuracy|precision|recall|f1)[:\s]*(\d+\.?\d*%?)", re.I), "metric"),
                (re.compile(r"(?:significant|p\s*[<>=]\s*\d+\.?\d*)", re.I), "significance"),
            ]
            for i, line in enumerate(c.split("\n"), 1):
                for pat, ftype in patterns:
                    m = pat.search(line)
                    if m:
                        results.append({"type": ftype, "content": m.group(0)[:200], "file": str(path), "line": i})
        except: pass
        return results

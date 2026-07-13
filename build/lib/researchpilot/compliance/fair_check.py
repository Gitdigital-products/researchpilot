"""FAIR data compliance checker."""
from pathlib import Path
class FAIRCheck:
    def check(self, path: Path) -> dict:
        checks = []
        has_data = any(f.suffix in (".csv",".json",".parquet",".h5",".xlsx") for f in path.rglob("*") if f.is_file())
        checks.append({"standard": "F1", "name": "Findable", "passed": has_data, "detail": "Data files present" if has_data else "No data files"})
        has_metadata = any("metadata" in f.name.lower() or f.name.endswith("-meta.json") for f in path.rglob("*") if f.is_file())
        checks.append({"standard": "F2", "name": "Metadata", "passed": has_metadata, "detail": "Metadata found" if has_metadata else "No metadata files"})
        has_doi = False
        for f in path.rglob("*.md"):
            try:
                if "doi:" in f.read_text(errors="ignore").lower(): has_doi = True
            except: pass
        checks.append({"standard": "F3", "name": "Persistent identifier", "passed": has_doi, "detail": "DOI reference found" if has_doi else "No DOI references"})
        has_license = any(f.name.startswith("LICENSE") for f in path.iterdir() if f.is_file()) if path.is_dir() else False
        checks.append({"standard": "R1", "name": "Licensed", "passed": has_license, "detail": "License present" if has_license else "No license"})
        has_readme = any(f.name.startswith("README") for f in path.iterdir() if f.is_file()) if path.is_dir() else False
        checks.append({"standard": "A1", "name": "Accessible", "passed": has_readme, "detail": "Documentation present" if has_readme else "No documentation"})
        has_code = any(f.suffix == ".py" for f in path.rglob("*") if f.is_file())
        checks.append({"standard": "I1", "name": "Interoperable", "passed": has_code, "detail": "Code available" if has_code else "No code"})
        return {"checks": checks, "passed": all(c["passed"] for c in checks), "total": len(checks)}

"""Research synthesis engine."""
from pathlib import Path
class Synthesizer:
    def synthesize(self, path: Path) -> dict:
        themes = []; gaps = []; consensus = []
        all_text = ""
        for f in list(path.rglob("*.md")) + list(path.rglob("*.txt")):
            try: all_text += f.read_text(errors="ignore") + "\n"
            except: pass
        import re
        methods = set(re.findall(r"(?:method(?:ology)?|approach|technique)[:\s]*(\w+(?:\s+\w+){0,3})", all_text, re.I))
        datasets = set(re.findall(r"(?:dataset|data(?:set)?|corpus)[:\s]*(\w+(?:\s+\w+){0,2})", all_text, re.I))
        if methods: themes.append(f"Research methods identified: {', '.join(list(methods)[:5])}")
        if datasets: themes.append(f"Datasets referenced: {', '.join(list(datasets)[:5])}")
        has_code = any("github.com" in f.read_text(errors="ignore") for f in path.rglob("*") if f.is_file() and ".venv" not in str(f))
        if not has_code: gaps.append("No code repositories referenced (reproducibility concern)")
        has_data = any(f.suffix in (".csv", ".json", ".parquet", ".h5") for f in path.rglob("*") if f.is_file())
        if not has_data: gaps.append("No raw data files found")
        return {"themes": themes, "gaps": gaps, "consensus": consensus, "methods": list(methods)[:10], "datasets": list(datasets)[:10], "has_code": has_code, "has_data": has_data}

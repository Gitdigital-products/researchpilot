"""Reproducibility checker."""
from pathlib import Path
class ReproducibilityChecker:
    def check(self, path: Path) -> dict:
        checks = []
        has_data = any(f.suffix in (".csv",".json",".parquet",".h5",".hdf5",".xlsx") for f in path.rglob("*") if f.is_file())
        checks.append({"name": "Raw data available", "passed": has_data, "detail": "Data files found" if has_data else "No raw data files"})
        has_code = any(f.suffix == ".py" for f in path.rglob("*") if f.is_file() and ".venv" not in str(f))
        checks.append({"name": "Analysis code available", "passed": has_code, "detail": "Python scripts found" if has_code else "No analysis code"})
        has_req = any(f.name in ("requirements.txt","pyproject.toml","environment.yml","Pipfile") for f in path.iterdir() if f.is_file()) if path.is_dir() else False
        checks.append({"name": "Dependencies specified", "passed": has_req, "detail": "Dependency file found" if has_req else "No requirements file"})
        has_readme = any(f.name.startswith("README") for f in path.iterdir() if f.is_file()) if path.is_dir() else False
        checks.append({"name": "Documentation", "passed": has_readme, "detail": "README found" if has_readme else "No README"})
        has_license = any(f.name.startswith("LICENSE") for f in path.iterdir() if f.is_file()) if path.is_dir() else False
        checks.append({"name": "License", "passed": has_license, "detail": "License found" if has_license else "No license"})
        has_notebook = any(f.suffix in (".ipynb",) for f in path.rglob("*") if f.is_file())
        checks.append({"name": "Notebook or pipeline", "passed": has_notebook or has_code, "detail": "Reproducible pipeline found" if has_notebook or has_code else "No notebook or script"})
        return {"checks": checks, "passed": all(c["passed"] for c in checks), "total": len(checks), "passed_count": sum(1 for c in checks if c["passed"])}

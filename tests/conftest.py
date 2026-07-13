"""Shared test fixtures for ResearchPilot."""

from pathlib import Path
from datetime import datetime
import pytest


@pytest.fixture
def sample_papers_dir(tmp_path: Path) -> Path:
    """Create a directory of sample research papers."""
    papers = tmp_path / "papers"
    papers.mkdir()

    (papers / "paper1.md").write_text(
        "# Machine Learning for Climate Modeling\n\n"
        "## Abstract\n"
        "We present a novel deep learning approach for climate modeling. "
        "Our method achieves 94.2% accuracy in predicting temperature anomalies. "
        "Keywords: climate, machine learning, deep learning, prediction\n\n"
        "## Method\n"
        "Our methodology uses a transformer-based architecture trained on "
        "the ERA5 dataset spanning 40 years.\n\n"
        "## Results\n"
        "We demonstrate significant improvements over baseline methods. "
        "Our model achieves p < 0.001 significance level.\n\n"
        "## References\n"
        "[1] Smith et al. (2020) doi:10.1038/s41586-020-2649-2\n"
        "[2] Johnson et al. (2019) Nature Climate Change\n"
    )

    (papers / "paper2.md").write_text(
        "# CRISPR Gene Editing Advances\n\n"
        "## Abstract\nWe review recent advances in CRISPR-Cas9 gene editing. "
        "Keywords: CRISPR, gene editing, biotechnology\n\n"
        "## Dataset\n"
        "Data from the ENCODE project and GTEx consortium were analyzed. "
        "The dataset is available at https://github.com/example/crispr-data\n\n"
        "## Results\n"
        "Our finding shows that off-target effects can be reduced by 87.3%. "
        "Precision: 96.2% Recall: 94.1% F1: 95.1%\n\n"
        "## References\n"
        "doi:10.1126/science.aav7973 (2021)\n"
        "doi:10.1038/nbt.4324 (2018)\n"
    )

    (papers / "metadata.json").write_text(
        '{"study": "climate-2024", "doi": "10.1234/climate.2024.001", "authors": ["Alice", "Bob"]}'
    )

    return papers


@pytest.fixture
def sample_data_dir(tmp_path: Path) -> Path:
    """Create a directory with data files for FAIR checking."""
    d = tmp_path / "research_data"
    d.mkdir()
    (d / "measurements.csv").write_text("x,y,z\n1,2,3\n4,5,6\n")
    (d / "metadata.json").write_text('{"description": "test data", "doi": "10.1234/test"}')
    (d / "analysis.py").write_text("import pandas as pd\nprint('analysis complete')\n")
    (d / "README.md").write_text("# Research Data\nSample research data")
    (d / "LICENSE").write_text("Apache-2.0")
    (d / "requirements.txt").write_text("numpy>=1.20\npandas>=1.3")
    return d


@pytest.fixture
def incomplete_dir(tmp_path: Path) -> Path:
    """Create a directory missing reproducibility requirements."""
    d = tmp_path / "incomplete"
    d.mkdir()
    (d / "results.txt").write_text("Some results without data or code\n")
    return d

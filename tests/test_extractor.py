"""Tests for finding extractor."""

from pathlib import Path
from researchpilot.analyzers.extractor import FindingExtractor


def test_extract_findings(sample_papers_dir):
    extractor = FindingExtractor()
    result = extractor.extract(sample_papers_dir)
    assert result["total"] > 0
    assert any(f["type"] == "metric" for f in result["findings"])


def test_extract_single_file(sample_papers_dir):
    extractor = FindingExtractor()
    result = extractor.extract(sample_papers_dir / "paper1.md")
    assert result["total"] > 0


def test_extract_contributions(sample_papers_dir):
    extractor = FindingExtractor()
    result = extractor.extract(sample_papers_dir)
    contribution_types = [f["type"] for f in result["findings"]]
    assert "contribution" in contribution_types or "result" in contribution_types


def test_extract_metrics(sample_papers_dir):
    extractor = FindingExtractor()
    result = extractor.extract(sample_papers_dir)
    metrics = [f for f in result["findings"] if f["type"] == "metric"]
    assert len(metrics) > 0

"""Tests for literature review analyzer."""

from pathlib import Path
from researchpilot.analyzers.literature import LiteratureAnalyzer


def test_analyze_papers(sample_papers_dir):
    analyzer = LiteratureAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    assert result["total"] == 2
    assert result["papers"][0]["title"] in ["Machine Learning for Climate Modeling", "CRISPR Gene Editing Advances"]
    assert result["avg_references"] >= 0


def test_analyze_empty_dir(tmp_path):
    analyzer = LiteratureAnalyzer()
    result = analyzer.analyze(tmp_path)
    assert result["total"] == 0
    assert result["avg_references"] == 0


def test_extract_keywords(sample_papers_dir):
    analyzer = LiteratureAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    paper1 = [p for p in result["papers"] if "Machine Learning" in p["title"]][0]
    assert len(paper1["keywords"]) > 0


def test_count_references(sample_papers_dir):
    analyzer = LiteratureAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    assert any(p["reference_count"] > 0 for p in result["papers"])

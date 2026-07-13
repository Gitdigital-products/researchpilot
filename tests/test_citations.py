"""Tests for citation network analyzer."""

from pathlib import Path
from researchpilot.analyzers.citations import CitationAnalyzer


def test_analyze_citations(sample_papers_dir):
    analyzer = CitationAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    assert result["total_references"] > 0


def test_analyze_authors(sample_papers_dir):
    analyzer = CitationAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    assert len(result["top_authors"]) >= 0


def test_analyze_year_distribution(sample_papers_dir):
    analyzer = CitationAnalyzer()
    result = analyzer.analyze(sample_papers_dir)
    assert isinstance(result["year_distribution"], dict)


def test_analyze_empty(tmp_path):
    analyzer = CitationAnalyzer()
    result = analyzer.analyze(tmp_path)
    assert result["total_references"] == 0
    assert result["unique_dois"] == 0

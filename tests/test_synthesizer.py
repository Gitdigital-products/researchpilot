"""Tests for research synthesizer."""

from pathlib import Path
from researchpilot.analyzers.synthesizer import Synthesizer


def test_synthesize_themes(sample_papers_dir):
    synth = Synthesizer()
    result = synth.synthesize(sample_papers_dir)
    assert isinstance(result["themes"], list)


def test_synthesize_gaps(sample_papers_dir):
    synth = Synthesizer()
    result = synth.synthesize(sample_papers_dir)
    assert isinstance(result["gaps"], list)


def test_synthesize_methods(sample_papers_dir):
    synth = Synthesizer()
    result = synth.synthesize(sample_papers_dir)
    assert isinstance(result["methods"], list)


def test_synthesize_returns_structure(sample_papers_dir):
    synth = Synthesizer()
    result = synth.synthesize(sample_papers_dir)
    assert "themes" in result
    assert "gaps" in result
    assert "methods" in result
    assert "datasets" in result
    assert "has_code" in result
    assert "has_data" in result


def test_synthesize_empty(tmp_path):
    synth = Synthesizer()
    result = synth.synthesize(tmp_path)
    assert len(result["methods"]) == 0
    assert len(result["datasets"]) == 0

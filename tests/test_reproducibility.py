"""Tests for reproducibility checker."""

from pathlib import Path
from researchpilot.analyzers.reproducibility import ReproducibilityChecker


def test_check_complete(sample_data_dir):
    checker = ReproducibilityChecker()
    result = checker.check(sample_data_dir)
    assert result["passed"] is True
    assert result["passed_count"] == result["total"]


def test_check_incomplete(incomplete_dir):
    checker = ReproducibilityChecker()
    result = checker.check(incomplete_dir)
    assert result["passed"] is False
    assert result["passed_count"] < result["total"]


def test_check_has_data(sample_data_dir):
    checker = ReproducibilityChecker()
    result = checker.check(sample_data_dir)
    data_check = [c for c in result["checks"] if c["name"] == "Raw data available"][0]
    assert data_check["passed"] is True


def test_check_has_code(sample_data_dir):
    checker = ReproducibilityChecker()
    result = checker.check(sample_data_dir)
    code_check = [c for c in result["checks"] if c["name"] == "Analysis code available"][0]
    assert code_check["passed"] is True


def test_check_has_license(sample_data_dir):
    checker = ReproducibilityChecker()
    result = checker.check(sample_data_dir)
    license_check = [c for c in result["checks"] if c["name"] == "License"][0]
    assert license_check["passed"] is True

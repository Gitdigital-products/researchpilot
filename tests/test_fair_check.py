"""Tests for FAIR data compliance checker."""

from pathlib import Path
from researchpilot.compliance.fair_check import FAIRCheck


def test_fair_check_finds_data(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    findable = [c for c in result["checks"] if c["standard"] == "F1"][0]
    assert findable["passed"] is True


def test_fair_check_metadata(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    metadata = [c for c in result["checks"] if c["standard"] == "F2"][0]
    assert metadata["passed"] is True


def test_fair_check_license(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    license_check = [c for c in result["checks"] if c["standard"] == "R1"][0]
    assert license_check["passed"] is True


def test_fair_check_accessible(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    accessible = [c for c in result["checks"] if c["standard"] == "A1"][0]
    assert accessible["passed"] is True


def test_fair_check_interoperable(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    interop = [c for c in result["checks"] if c["standard"] == "I1"][0]
    assert interop["passed"] is True


def test_fair_check_missing_data(incomplete_dir):
    checker = FAIRCheck()
    result = checker.check(incomplete_dir)
    assert result["passed"] is False


def test_fair_check_total_checks(sample_data_dir):
    checker = FAIRCheck()
    result = checker.check(sample_data_dir)
    assert result["total"] == 6

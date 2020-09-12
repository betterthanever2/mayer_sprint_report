#!/usr/bin/env python

"""Tests for `mayer_sprint_report` package."""


import unittest
from click.testing import CliRunner

from mayer_sprint_report import mayer_sprint_report
from mayer_sprint_report import cli


class TestMayer_sprint_report(unittest.TestCase):
    """Tests for `mayer_sprint_report` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'mayer_sprint_report.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

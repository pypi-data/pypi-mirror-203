"""Tests for `classifyawsetsjsonbyregion` package."""
from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from classifyawsetsjsonbyregion import cli


def test_command_line_interface(configured_cli_runner: CliRunner) -> None:
    """Tests the CLI.

    Checks that:
    - the CLI returns empty output
    - the CLI returns 0 exit code
    - the CLI creates the expected number of files
    - the CLI creates the expected files
    - the CLI creates the expected files with the expected content
    """
    expected = {
        "awsets-other-regions-ap-northeast-2.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-ap-northeast-3.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-ap-south-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-ap-southeast-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-ap-southeast-2.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-aws-global.csv": "",
        "awsets-other-regions-ca-central-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-eu-central-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-eu-north-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-eu-west-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-eu-west-2.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-eu-west-3.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-sa-east-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-us-east-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-us-east-2.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-us-west-1.csv": "athena/datacatalog AwsDataCatalog {}\n",
        "awsets-other-regions-us-west-2.csv": "athena/datacatalog AwsDataCatalog {}\n",
    }
    result = configured_cli_runner.invoke(cli.main)
    # Reason: Check that output is empty.
    assert result.output == ""  # noqa: PLC1901
    assert result.exit_code == 0
    list_output_file = list((Path.cwd() / "output").iterdir())
    assert_output_files(expected, list_output_file)


def assert_output_files(expected: dict[str, str], list_output_file: list[Path]) -> None:
    assert len(list_output_file) == len(expected)
    for output_file, (expected_file_name, expected_json) in zip(sorted(list_output_file), expected.items()):
        assert output_file.name == expected_file_name
        assert output_file.read_text() == expected_json


def test_help() -> None:
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output

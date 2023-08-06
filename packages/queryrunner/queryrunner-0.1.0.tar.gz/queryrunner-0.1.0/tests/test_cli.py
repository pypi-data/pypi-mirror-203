from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from typer.testing import CliRunner

from queryrunner.cli import app

EXAMPLE_URI = "sqlite:///:memory:"
EXAMPLE_SQL = "SELECT 'Value1' AS col1"


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_show(runner):
    result = runner.invoke(app, ["show", EXAMPLE_URI, EXAMPLE_SQL])
    assert result.exit_code == 0


def test_cli_show_extra_params(runner):
    result = runner.invoke(
        app, ["show", EXAMPLE_URI, "SELECT '5' as col1 WHERE col1=:val", "--val", "5"]
    )
    assert result.exit_code == 0


def test_cli_to_csv(runner):
    with TemporaryDirectory() as tmpdirname:
        output_path = Path(tmpdirname) / "output.csv"
        result = runner.invoke(
            app, ["to-csv", EXAMPLE_URI, EXAMPLE_SQL, str(output_path)]
        )
        assert result.exit_code == 0
        assert "Created" in result.stdout
        assert output_path.exists()


def test_cli_to_ndjson(runner):
    with TemporaryDirectory() as tmpdirname:
        output_path = Path(tmpdirname) / "output.ndjson"
        result = runner.invoke(
            app, ["to-ndjson", EXAMPLE_URI, EXAMPLE_SQL, str(output_path)]
        )
        assert result.exit_code == 0
        assert "Created" in result.stdout
        assert output_path.exists()

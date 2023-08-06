from pathlib import Path

from queryrunner.query import parse_database_uri, parse_query, query_data


def test_uri_parsing():
    assert parse_database_uri("sqlite:///") == "sqlite:///"
    assert parse_database_uri("TEST_DB") == "sqlite:///:memory:"


def test_sql_parsing():
    assert parse_query("SELECT * FROM Table1") == "SELECT * FROM Table1"
    fp = "tests/example-query.sql"
    assert parse_query(fp) == "SELECT 'Value1' AS col1, 'Value2' as col2"
    fp = Path("tests/example-query.sql")
    assert parse_query(fp) == "SELECT 'Value1' AS col1, 'Value2' as col2"


def test_running_query():
    fp = Path("tests/example-query.sql")
    table = query_data("TEST_DB", fp)
    assert table.column_names == ("col1", "col2")


def test_running_query_params():
    table = query_data("sqlite:///", "SELECT 'Value' AS col1 WHERE col1 = 'Value'")
    assert table.column_names == ("col1",)
    rows = [tuple(x) for x in table.rows]
    assert rows[0] == ("Value",)

    table = query_data(
        "sqlite:///",
        "SELECT 'Value' AS col1 WHERE col1 = :val",
        params={"val": "Value"},
    )
    assert table.column_names == ("col1",)
    rows = [tuple(x) for x in table.rows]
    assert rows[0] == ("Value",)

    table = query_data(
        "sqlite:///",
        "SELECT 'Value' AS col1 WHERE col1 = :val",
        params={"val": "NotValue"},
    )
    rows = [tuple(x) for x in table.rows]
    assert len(rows) == 0

import os
from pathlib import Path
from typing import Optional, Union

from agate import Table
from sqlalchemy import create_engine


def parse_database_uri(db_uri: str) -> str:
    """Get DB URI from env var if not already a sqlalchemy URI"""
    if "://" in db_uri:
        return db_uri

    db_uri = os.getenv(db_uri, "")
    if db_uri:
        return db_uri

    raise ValueError(f"'{db_uri}' is not a sqlalchemy dialect or environment variable")


def parse_query(query: Union[Path, str] = "") -> str:
    """Return back SQL or load from file if Path"""

    query_file: Optional[Path] = None
    if isinstance(query, Path):
        query_file = query
    else:
        tqf = Path(query)
        if tqf.exists():
            query_file = tqf

    if query_file:
        with open(query_file) as fh:
            return fh.read()

    if not query or not isinstance(query, str):
        raise ValueError("Need to specify either an SQL query or file containing query")

    return query


def query_data(
    db_uri: str = "",
    query: Union[Path, str] = "",
    params: Optional[dict] = None,
    echo: bool = True,
) -> Table:
    db_uri = parse_database_uri(db_uri)
    query = parse_query(query)

    engine = create_engine(db_uri, echo=echo)
    with engine.connect() as connection:
        with connection.begin():
            res = connection.exec_driver_sql(query, params)
            data = [dict(row._mapping.items()) for row in res]
            return Table.from_object(data)

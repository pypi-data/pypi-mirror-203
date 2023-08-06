from pathlib import Path

import typer

from .query import query_data

app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def show(
    db_uri: str,
    query: str,
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    extra_args = (x[2:] if x[0:2] == "--" else x for x in ctx.args)
    params = dict(zip(extra_args, extra_args))
    table = query_data(db_uri, query, params, echo=verbose)
    table.print_table(max_columns=3, max_rows=10)


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def to_csv(
    db_uri: str,
    query: str,
    output_file: Path,
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    extra_args = (x[2:] if x[0:2] == "--" else x for x in ctx.args)
    params = dict(zip(extra_args, extra_args))
    table = query_data(db_uri, query, params, echo=verbose)
    table.to_csv(output_file)
    typer.echo(f"Created {output_file}")


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def to_ndjson(
    db_uri: str,
    query: str,
    output_file: Path,
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    extra_args = (x[2:] if x[0:2] == "--" else x for x in ctx.args)
    params = dict(zip(extra_args, extra_args))
    table = query_data(db_uri, query, params, echo=verbose)
    table.to_json(output_file, newline=True)
    typer.echo(f"Created {output_file}")

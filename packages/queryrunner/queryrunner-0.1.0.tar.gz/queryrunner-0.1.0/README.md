# Query-Runner

CLI tool to help with running queries.

## Quickstart

Pass through a [sqlalchemy DB URL](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls) and a query to run a query and export to file. 
(You may need the relevant DB drivers installed also.)


```sh
python -m queryrunner show "sqlite:///" "SELECT 'Val' as col1"
python -m queryrunner to-csv "sqlite:///" "SELECT 'Val' as col1" "output.csv"
```

You can also use an environment variable to contain your connection string, and a file to contain your SQL query.

```env
DB_URI="sqlite:///"
```

```sql
# example-query.sql
SELECT 'Val' as col1
```

```sh
python -m queryrunner to-csv "DB_URI" "example-query.sql" "output.csv"
```

### Query Parameters

You can pass query parameters as extra CLI options, but this only works for strings.

So this will work:

```sh
python -m queryrunner show "sqlite:///" "SELECT '5' as col1 WHERE col1=:val" --val 5
python -m queryrunner show "sqlite:///" "SELECT 5 as col1 WHERE CAST(col1 as text)=:val" --val 5
```

But this will not:

```sh
python -m queryrunner show "sqlite:///" "SELECT 5 as col1 WHERE col1=:val" --val 5
```

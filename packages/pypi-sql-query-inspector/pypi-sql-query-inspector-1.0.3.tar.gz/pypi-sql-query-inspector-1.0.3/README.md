### SQL Inspector package
A simple example of django middleware package

### Usage
Append middleware to `MIDDLEWARES` list:
```
MIDDLEWARE = [
    ...
    'pypi_sql_query_inspector.print_sql_queries_to_terminal',
]
```

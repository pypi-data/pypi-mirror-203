### SQL Inspector package
A simple example of django middleware package

### Usage
Append middleware to `MIDDLEWARES` list:
```
MIDDLEWARE = [
    ...
    'pypi-sql-query-inspector.middleware.new_middleware',
]
```

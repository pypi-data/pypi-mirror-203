# dbxconfig

Configuration framework for databricks pipelines.
Define configuration and table dependencies in yaml config then get the table mappings config model:

```python
from dbxconfig import Config, Timeslice, StageType

# build path to configuration file
pattern = "auto_load_schema"
config_path = f"./Config/{pattern}.yaml"

# create a timeslice object for slice loading. Use * for all time (supports hrs, mins, seconds and sub-second).
timeslice = Timeslice(day="*", month="*", year="*")

# parse and create a config objects
config = Config(timeslice=timeslice, config_path=config_path)

# get the configuration for a table mapping to load.
table_mapping = config.get_table_mapping(
    timeslice=timeslice, 
    stage=StageType.raw, 
    table="customers"
)
```

## Development Setup

```
pip install -r requirements.txt
```

## Unit Tests

To run the unit tests with a coverage report.

```
pip install -e .
pytest test/unit --junitxml=junit/test-results.xml --cov=dbxconfig --cov-report=xml --cov-report=html
```

## Build

```
python setup.py sdist bdist_wheel
```

## Publish


```
twine upload dist/*
```

from dagster import Definitions, asset

@asset
def hello_dagster():
    """A simple test asset."""
    return "Dagster is working!"

defs = Definitions(
    assets=[hello_dagster]
)

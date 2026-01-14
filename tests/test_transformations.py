import sys
import os
import pytest
from pyspark.testing import assertDataFrameEqual

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.transformations.clean_data import clean_data

@pytest.fixture(scope="session")
def spark():
    from pyspark.sql import SparkSession
    return SparkSession.builder.remote("sc://localhost").appName("test").getOrCreate()

def test_clean_data(spark):
    data = [("Alice", 25), ("Bob", 30)]
    df = spark.createDataFrame(data, ["name", "age"])
    result = clean_data(df)
    assert result.count() == 2
    assert result.columns == ["name", "age"]

def test_dataframe_equality(spark):
    data = [("Alice", 25), ("Bob", None)]
    df = spark.createDataFrame(data, ["name", "age"])
    result = clean_data(df)
    expected_data = [("Alice", 25)]
    expected_df = spark.createDataFrame(expected_data, ["name", "age"])
    assertDataFrameEqual(expected_df, result)
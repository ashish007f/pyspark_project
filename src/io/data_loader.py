from pyspark.sql import SparkSession, DataFrame

def read_csv(spark: SparkSession, path: str) -> DataFrame:
    """
    Read a CSV file into a DataFrame.
    """
    return spark.read.csv(path, header=True, inferSchema=True)
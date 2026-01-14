from pyspark.sql.connect.session import SparkSession

def create_spark_session(app_name="ETL Job"):
    """
    Create and return a SparkSession using Spark Connect.
    """
    return SparkSession.builder.remote("sc://localhost") \
        .appName(app_name) \
        .getOrCreate()
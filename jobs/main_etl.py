import json
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.spark_setup import create_spark_session
from src.io.data_loader import read_csv
from src.transformations.clean_data import clean_data
from src.utils.logger import get_logger

def main():
    logger = get_logger(__name__)
    logger.info("Starting ETL job")

    with open('configs/etl_config.json') as f:
        config = json.load(f)

    # Make paths absolute
    config['csv_path'] = os.path.abspath(config['csv_path'])
    config['output_path'] = os.path.abspath(config['output_path'])

    spark = create_spark_session()
    logger.info("Spark session created")

    df = read_csv(spark, config['csv_path'])
    logger.info(f"Read CSV from {config['csv_path']}")

    df_clean = clean_data(df)
    logger.info("Data cleaned")

    logger.info("Top 10 rows:")
    df_clean.show(10)

    spark.stop()
    logger.info("ETL job completed")

if __name__ == "__main__":
    main()
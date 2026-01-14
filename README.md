# PySpark ETL Project

This project demonstrates a simple ETL job using PySpark to read a CSV file and display the top 10 rows.

## Project Structure

- `bin/`: Shell scripts for spark-submit or orchestration
- `configs/`: JSON/YAML files for job parameters
- `jobs/`: Main entry point scripts for cluster execution
- `src/`: Core application package
  - `transformations/`: Pure functions that take and return DataFrames
  - `utils/`: Helper modules like logging and SparkSession factory
  - `io/`: Reading from and writing to S3, HDFS, or databases
- `tests/`: Unit and integration tests
- `pyproject.toml`: Modern Python build and dependency management
- `requirements.txt`: List of Python dependencies

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure you have Apache Spark installed and the Spark Connect server running locally.

   To start the Spark Connect server:
   ```bash
   $SPARK_HOME/sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:3.4.0
   ```
   Replace `3.4.0` with your Spark version if different.

3. The project uses `pyspark-client` for connecting to the Spark Connect server.

## Running the ETL Job

1. Update `configs/etl_config.json` with the path to your CSV file.

2. Run the main ETL script:
   ```bash
   python jobs/main_etl.py
   ```

This will read the CSV file, apply transformations, and display the top 10 rows.

## Testing

Run tests with:
```bash
pytest tests/
```
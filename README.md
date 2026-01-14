# PySpark ETL Sample Project

This is a sample project created for demonstrating PySpark ETL operations. It showcases a simple ETL job using PySpark to read a CSV file and display the top 10 rows.

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

## Setup

1. Ensure you have `uv` installed for managing Python dependencies. Install it if needed:
   ```bash
   pip install uv
   ```
   Learn more about [uv](https://github.com/astral-sh/uv?tab=readme-ov-file)

2. Install Python dependencies using uv:
   ```bash
   uv sync
   ```

3. Ensure you have Apache Spark 4.1.1 installed and SPARK_HOME set and the Spark Connect server running locally.

   To start the Spark Connect server:
   ```bash
   $SPARK_HOME/sbin/start-connect-server.sh
   ```
   Learn more about [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html)

4. The project uses `pyspark-client` 4.1.1 for connecting to the Spark Connect server.

## Running the ETL Job

1. Update `configs/etl_config.json` with the path to your CSV file.

2. Run the main ETL script:
   ```bash
   uv run jobs/main_etl.py
   ```

This will read the CSV file, apply transformations, and display the top 10 rows.

## Testing

Run tests with:
```bash
uv run pytest tests/
```
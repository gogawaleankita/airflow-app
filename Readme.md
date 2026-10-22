# Airflow Demo Project

This project demonstrates:
- Airflow Basic Operators
- XCom usage
- Running Spark flows
- Running dbt flows

## Requirements
- Python 3.11.17
- apache-airflow==3.3.2

## Setup
1. Create and activate a Python virtual environment.
2. Install Airflow with pip.
3. Initialize Airflow metadata DB.
4. Start webserver and scheduler.
5. Place demo DAGs in `dags/` folder.

## Usage
- Run DAGs to test operators, XCom, Spark, and dbt.
- Validate outputs in Airflow UI and logs.
- Use `dbt docs generate` for lineage visualization.

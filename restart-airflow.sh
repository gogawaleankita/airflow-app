#!/bin/bash

# Navigate to your Airflow project root
cd /mnt/c/Users/ankit/PycharmProjects/airflow-app || exit

source airflow_env/bin/activate


# Stop any running Airflow processes
pkill -f "airflow scheduler"
pkill -f "airflow api-server"

# Reset and migrate the metadata DB
# airflow db reset -n
# airflow db migrate

# Start scheduler and API server fresh
airflow scheduler > /logs/scheduler/scheduler.log 2>&1 &
airflow api-server > /logs/api-server/api-server.log 2>&1 &

echo "Airflow restarted. Scheduler logs: /logs/scheduler/scheduler.log, API server logs: /logs/api-server/api-server.log"

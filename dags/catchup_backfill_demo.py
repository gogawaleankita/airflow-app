from airflow.sdk import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'ankita',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    default_args=default_args,
    catchup=True,
    tags=["demo"]
)
def catchup_backfill_demo_v1():

    @task()
    def print_date():
        print(f"Current execution date is: {datetime.now()}")
    
    t1= print_date()

catchup_backfill_demo_v1()


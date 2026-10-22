from airflow.sdk import dag, task
import pendulum

@dag(
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["demo"],
)
def taskflow_demo_v2():

    @task()
    def extract():
        return {"table": "customer_data", "partition": "2026-10-21"}

    @task()
    def transform(data: dict):
        return {"summary": f"Table {data['table']} partition {data['partition']}"}

    @task()
    def load(summary):
        print(f'summary =>>> {summary}')

    data = extract()
    summary = transform(data)
    load(summary)

taskflow_demo_v2()

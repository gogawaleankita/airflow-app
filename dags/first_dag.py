from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator



def greet():
    print("Hello, Airflow from greet method()!")

with DAG(
    dag_id="first_dag",
    schedule="@daily",   # ✅ use `schedule` not `schedule_interval`
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    bash_task = BashOperator(
        task_id="bash_taskV1",
        bash_command="echo Hello, Airflow!"
    )
    bash_task2 = BashOperator(
        task_id="bash_taskv1",
        bash_command="echo Hello, Airflow! !2"
    )

    py_task = PythonOperator(
        task_id="py_taskV1",
        python_callable=greet
    )

    # bash_task >> bash_task2 >> py_task

    bash_task >> [py_task,bash_task2]  # ✅ This is a valid way to set dependencies

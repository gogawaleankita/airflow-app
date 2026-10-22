from airflow import DAG 
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator

def greet(name,age):
    print(f"###Hello, Airflow from greet method()\n! My name is {name} and I am {age} years old.###")
    return f"Hello, Airflow from greet method()! My name is {name} and I am {age} years old."

def get_name():
    return "AnkitaG"
    

default_args = {
'owner':'ankita',
'retries':5,
'retry_delay':timedelta(minutes=5),
}

with DAG(
    dag_id="create_dag_withpython_op_v1",
    default_args=default_args,
    schedule="@daily",   # ✅ use `schedule` not `schedule_interval`
    description='This is my first dag with python operator',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    py_task = PythonOperator(
        task_id="py_taskV1",
        python_callable=greet,
        op_args=['Ankita', 28]
    )
    py_task
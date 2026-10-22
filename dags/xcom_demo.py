from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ankita',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}


def getFullName(ti):
    ti.xcom_push(key='name', value='Ankita')
    ti.xcom_push(key='last_name', value='Ghosh')

def get_age(age):
    return age



def greet_with_xcom(ti):
    fname = ti.xcom_pull(task_ids='getFullName',key='name')
    lname = ti.xcom_pull(task_ids='getFullName',key='last_name')
    age = ti.xcom_pull(task_ids='get_age')

    print( f"Hello, Airflow from greet_with_xcom method()! My name is {fname} {lname} and I am {age} years old.")

with DAG(
    dag_id="xcom_demo_v6",  
    default_args=default_args,
    schedule="@daily",   # ✅ use `schedule` not `schedule_interval`
    description='This is my first dag with python operator for x_com demo',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:
    py_task1 = PythonOperator(
        task_id="getFullName", 
        python_callable=getFullName)
    
    py_task2 = PythonOperator(
        task_id="get_age",
        python_callable=get_age,
        op_kwargs={"age": 28}
    )

    py_task3 = PythonOperator(
        task_id="greet",
        python_callable=greet_with_xcom
    )

    [py_task1, py_task2] >> py_task3


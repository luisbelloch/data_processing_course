from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world!'

dag = DAG(
    'hello_python_operator',
    description='Simple tutorial DAG',
    schedule_interval='20 * * * *',
    start_date=datetime(2017, 3, 20),
    catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_from_python', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator

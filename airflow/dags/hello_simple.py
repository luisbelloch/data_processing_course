from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {"start_date": datetime(2019, 2, 5)}
dag = DAG('hello', default_args=default_args, schedule_interval=None, tags=['upv'],)

dummy_operator = DummyOperator(task_id='dummy_task', dag=dag)
hello_operator = DummyOperator(task_id='hello_task', dag=dag)

dummy_operator >> hello_operator

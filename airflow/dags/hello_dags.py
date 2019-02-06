from builtins import range
from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

dag = DAG('hello_dags', schedule_interval=None, start_date=airflow.utils.dates.days_ago(2))

def print_hello():
    return 'Hello world!'

inicio = BashOperator(task_id='inicio', bash_command="echo inicio!", dag=dag)
paso1 = BashOperator(task_id='paso1', bash_command="echo paso 1", dag=dag)
paso2 = PythonOperator(task_id='paso2', python_callable=print_hello, dag=dag)
paso3 = DummyOperator(task_id='paso3', dag=dag)
ultima_tarea = DummyOperator(task_id='ultima_tarea', dag=dag)

inicio >> paso1
inicio >> paso3
paso1 >> paso2 >> ultima_tarea
paso3 >> ultima_tarea

if __name__ == "__main__":
    dag.cli()

import os
from datetime import datetime

from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.models.variable import Variable
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'patatas')

@task(task_id="do_something")
def do_something():
  print("Something!")

with DAG(
  dag_id='s3_file_sensor',
  schedule_interval=None,
  start_date=datetime(2021, 1, 1),
  catchup=False,
  default_args={"bucket_name": BUCKET_NAME},
  max_active_runs=1,
  tags=['upv'],
) as dag:

  op = S3KeySensor(task_id="s3_key_sensor", bucket_key="s3://gasolina/some_file.json", bucket_name=None, dag=dag)
  end_task = do_something()
  op >> end_task

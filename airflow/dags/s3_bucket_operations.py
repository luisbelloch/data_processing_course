import os
from datetime import datetime

from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator, S3DeleteBucketOperator

# By default, it will use 'aws_default' connection. You can create it here by running `make minio_credentials`
# If you want to change it, use a variable and pass it as `aws_conn_id` to all AWS operators.
AWS_CONN_ID = 'aws_default'

BUCKET_NAME = os.environ.get('BUCKET_NAME', 'patatas')

@task(task_id="s3_bucket_dag_add_keys_to_bucket")
def upload_keys():
  s3_hook = S3Hook()
  for i in range(0, 3):
    s3_hook.load_string(string_data="input", key=f"path/data{i}", bucket_name=BUCKET_NAME)

with DAG(
  dag_id='s3_bucket_operations',
  schedule_interval=None,
  start_date=datetime(2021, 1, 1),
  catchup=False,
  default_args={"bucket_name": BUCKET_NAME},
  max_active_runs=1,
  tags=['upv'],
) as dag:

  create_bucket = S3CreateBucketOperator(task_id='s3_bucket_dag_create', region_name='us-east-1')
  add_keys_to_bucket = upload_keys()
  delete_bucket = S3DeleteBucketOperator(task_id='s3_bucket_dag_delete', force_delete=True)
  create_bucket >> add_keys_to_bucket >> delete_bucket

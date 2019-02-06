import datetime
import os

from airflow import models
from airflow.contrib.operators import dataproc_operator
from airflow.utils import trigger_rule

output_file = os.path.join(
  models.Variable.get('gcs_bucket'), 'dataproc_simple',
  datetime.datetime.now().strftime('%Y%m%d-%H%M%S')) + os.sep

yesterday = datetime.datetime.combine(
  datetime.datetime.today() - datetime.timedelta(1),
  datetime.datetime.min.time())

args = {
  'start_date': yesterday,
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': datetime.timedelta(minutes=5),
  'project_id': models.Variable.get('gcp_project')
}

with models.DAG('spark_simple', schedule_interval=datetime.timedelta(days=1), default_args=args) as dag:
  run_step = dataproc_operator.DataProcPySparkOperator(
      task_id='run_spark',
      cluster_name='cluster-9c11',
      region='europe-west1',
      main='gs://bigdataupv_code/compras_top_ten_countries.py',
      files=['gs://bigdataupv_code/helpers.py'])


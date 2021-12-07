import json
import socket

from datetime import datetime

from airflow import AirflowException
from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor

import boto3
import botocore.client
import requests

codigo_postal = "50197"
bucket_name = "gasolina"
endpoint = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

def s3_resource():
  return boto3.resource('s3',
        endpoint_url='http://minio:9000',
        aws_access_key_id='bigdataupv',
        aws_secret_access_key='bigdataupv',
        config=botocore.client.Config(signature_version='s3v4'), region_name='us-east-1')

def read_json_from_s3(key):
  obj = s3_resource().Object(bucket_name, key)
  return json.loads(obj.get()['Body'].read().decode('utf-8'))

def save_to_s3(key, data):
  obj = s3_resource().Object(bucket_name, key)
  obj.put(Body=data)

@dag(schedule_interval=None, start_date=datetime(2021, 1, 1), catchup=False, tags=['upv'])
def extraer_precio_gasolina_s3():

  @task
  def recogida_s3():
    print("Recogiendo datos...")
    response = requests.get(endpoint)
    if response.status_code != 200:
      AirflowException(f"Fallo de conexión {response.status_code}")

    filename = f'recogida-{datetime.now().strftime("%Y%m%d%H%M%S")}.json'
    save_to_s3(filename, response.text)
    return { "recogida": filename }

  @task
  def filtrado_s3(contexto, codigo_postal):
    print("Filtrando datos...")

    datos = read_json_from_s3(contexto['recogida'])
    filtrados = list(filter(lambda x: x['C.P.'] == codigo_postal, datos['ListaEESSPrecio']))

    filename = f'filtrado-{datetime.now().strftime("%Y%m%d%H%M%S")}.json'
    save_to_s3(filename, json.dumps(filtrados))

    return { **contexto, "filtrado": filename }

  @task
  def almacenamiento_s3(contexto):
    print("Almacenando datos... Nothing to do!")
    import socket
    print("hostname:", socket.gethostname())
    return 42

  todos_los_datos = recogida_s3()
  datos_del_codigo_postal_x = filtrado_s3(todos_los_datos, codigo_postal)
  almacenamiento_s3(datos_del_codigo_postal_x)

dag_gasolina = extraer_precio_gasolina_s3()

# Additionally, use Amazon operator, particularly S3KeySensor
# https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/s3.html

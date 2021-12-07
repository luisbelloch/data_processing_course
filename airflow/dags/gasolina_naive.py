import json
from datetime import datetime

from airflow import AirflowException
from airflow.decorators import dag, task

import requests

codigo_postal = "50197"
endpoint = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

@dag(schedule_interval=None, start_date=datetime(2021, 1, 1), catchup=False, tags=['upv'])
def extraer_precio_gasolina_naive():

  @task
  def recogida():
    print("Recogiendo datos...")
    response = requests.get(endpoint)
    if response.status_code != 200:
      AirflowException(f"Fallo de conexión {response.status_code}")

    datos = response.json()
    return datos['ListaEESSPrecio']

  @task
  def filtrado(datos, codigo_postal):
    return list(filter(lambda x: x['C.P.'] == codigo_postal, datos))

  @task
  def almacenamiento(datos):
    print("Almacenando datos...")
    print(json.dumps(datos, indent=2))

  todos_los_datos = recogida()
  datos_del_codigo_postal_x = filtrado(todos_los_datos, codigo_postal)
  almacenamiento(datos_del_codigo_postal_x)

dag_gasolina = extraer_precio_gasolina_naive()


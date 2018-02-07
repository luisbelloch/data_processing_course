import os
import pytest

from contenedores import *
from pyspark.sql import SQLContext

def test_ejercicio_3_data_frame_tiene_613_filas(resultados_ejercicio_3):
  assert 613 == resultados_ejercicio_3.rdd.count()

def test_ejercicio_3_data_frame_tiene_al_menos_una_fila_correcta(resultados_ejercicio_3):
  df = resultados_ejercicio_3
  assert 1 == df.filter(df.ship_imo == "JMP1637582").filter(df.container_id == "XPOG1294738").rdd.count()

def test_ejercicio_3_resultados_guardados(resultados_ejercicio_3, comprobar_hdfs):
  assert comprobar_hdfs(3) == True

def test_ejercicio_3_estructura_dataframe_correcta(resultados_ejercicio_3, tiene_columnas):
  tiene_columnas(resultados_ejercicio_3, ['contact', 'container_group', 'container_id', 'container_type', 'country', 'customs_ok', 'declared', 'departure', 'gross_weight', 'net_weight', 'owner', 'ship_imo', 'ship_name'])


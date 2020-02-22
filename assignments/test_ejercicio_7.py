import os
import pytest

from .contenedores import *

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_7(spark_context, path_resultados)

def test_ejercicio_7_resultados_guardados(resultados, comprobar_hdfs):
  assert comprobar_hdfs(7) == True

def test_ejercicio_7_estructura_dataframe_correcta(resultados, tiene_columnas):
  tiene_columnas(resultados, ['container_group', 'ship_imo', 'ship_name', 'total_net_weight'])


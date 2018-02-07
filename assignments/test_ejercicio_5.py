import os
import pytest

from contenedores import *

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_5(spark_context, path_resultados)

def test_ejercicio_5_existen_605_contenedores(resultados):
  assert 605 == resultados.rdd.count()

def test_ejercicio_5_al_menos_uno_de_los_contenedores_validos_existe_en_la_lista(resultados):
  assert any([e["propietario"] == "UFC" and e["numero_serie"] == "118653" for e in resultados.rdd.collect()])

def test_ejercicio_5_todos_los_contendores_invalidos_estan_excluidos(resultados):
  existentes = resultados.select(resultados["container_id"]).rdd.collect()
  excluidos = [u'GJFL14A2798', u'CTVU1506A832', u'IJWDR1216916', u'OKANR1240284', u'JMYG190Z978', u'DUKF166276', u'']
  assert all([(e not in excluidos) for e in existentes])

def test_ejercicio_5_resultados_guardados(resultados, comprobar_hdfs):
  assert comprobar_hdfs(5) == True

def test_ejercicio_5_estructura_dataframe_correcta(resultados, tiene_columnas):
  tiene_columnas(resultados, ['categoria', 'container_id', 'digito_control', 'numero_serie', 'propietario', 'ship_imo'])


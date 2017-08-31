
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_5(spark_context, path_resultados)

def test_ejercicio_5_estructura_dataframe_correcta(spark_context, path_resultados, resultados):

  correct = ['categoria', 'container_id', 'digito_control', 'numero_serie', 'propietario', 'ship_imo']
  returned = sorted([column.lower() for column in resultados.columns])

  assert correct == returned

def test_ejercicio_5_resultados_guardados_formato_texto(spark_context, path_resultados, resultados):

  path = path_resultados(5)

  assert os.path.isfile(path) == True

  assert os.stat(path).st_size > 0L


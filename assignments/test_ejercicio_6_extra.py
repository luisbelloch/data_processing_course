
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_6(spark_context, path_resultados)

def test_ejercicio_6_estructura_dataframe_correcta(spark_context, path_resultados, resultados):

  correct = ['container', 'ship_imo', 'ship_name', 'total_net_weight']
  returned = sorted([column.lower() for column in resultados.columns])

  assert correct == returned

def test_ejercicio_6_resultados_guardados_formato_texto(spark_context, path_resultados, resultados):

  path = path_resultados(6)

  assert os.path.isfile(path) == True

  assert os.stat(path).st_size > 0L


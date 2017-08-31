
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os
from pyspark.sql import SQLContext

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_4(spark_context, path_resultados)

def test_ejercicio_4_resultados_guardados_formato_json_y_estructura_dataframe_correcta(spark_context, path_resultados, resultados):

  path = path_resultados(4)

  assert os.path.isdir(path) == True

  sqlContext = SQLContext(spark_context)

  df = sqlContext.read.json(path)
  
  assert df.count() == 20

  correct = ['ship_imo']
  returned = [column.lower() for column in df.columns]

  assert correct == returned


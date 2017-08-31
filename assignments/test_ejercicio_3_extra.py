
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os
from pyspark.sql import SQLContext

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_3(spark_context, path_resultados)

def test_ejercicio_3_resultados_guardados_formato_parquet_y_estructura_dataframe_correcta(spark_context, path_resultados, resultados):

  path = path_resultados(3)

  assert os.path.isdir(path) == True

  sqlContext = SQLContext(spark_context)

  df = sqlContext.read.parquet(path)
  
  assert df.count() == 613

  correct = ['contact', 'container_group', 'container_id', 'container_type', 'country', 'customs_ok', 'declared', 'departure', 'gross_weight', 'net_weight', 'owner', 'ship_imo', 'ship_name']
  returned = sorted([column.lower() for column in df.columns])

  assert correct == returned


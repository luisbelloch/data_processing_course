#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

from contenedores import *

# from pyspark.sql import SQLContext

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_7(spark_context, path_resultados)

def test_ejercicio_7_resultados_guardados(comprobar_hdfs):
  assert comprobar_hdfs(7) == True

# def test_ejercicio_7_resultados_guardados_formato_parquet_y_estructura_dataframe_correcta(spark_context, path_resultados):

#   ejercicio_7(spark_context, path_resultados)

#   path = path_resultados(7)

#   assert os.path.isdir(path) == True

#   sqlContext = SQLContext(spark_context)

#   df = sqlContext.read.parquet(path)
  
#   assert df.count() == 261

#   correct = ['container', 'ship_imo', 'ship_name', 'total_net_weight']
#   returned = sorted([column.lower() for column in df.columns])

#   assert correct == returned


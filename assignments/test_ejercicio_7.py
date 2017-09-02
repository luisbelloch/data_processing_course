
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os
from pyspark.sql import SQLContext

def test_ejercicio_7_resultados_guardados_formato_parquet_y_estructura_dataframe_correcta(spark_context, path_resultados):

  ejercicio_7(spark_context, path_resultados)

  path = path_resultados(7)

  assert os.path.isdir(path) == True

  sqlContext = SQLContext(spark_context)

  df = sqlContext.read.parquet(path)
  
  assert df.count() == 261

  correct = ['container', 'ship_imo', 'ship_name', 'total_net_weight']
  returned = sorted([column.lower() for column in df.columns])

  assert correct == returned


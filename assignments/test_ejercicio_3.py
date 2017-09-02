#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os
from pyspark.sql import SQLContext

def test_ejercicio_3_data_frame_tiene_613_filas(resultados_ejercicio_3):
  assert 613 == resultados_ejercicio_3.rdd.count()

def test_ejercicio_3_data_frame_tiene_al_menos_una_fila_correcta(resultados_ejercicio_3):
  df = resultados_ejercicio_3
  assert 1 == df.filter(df.ship_imo == "JMP1637582").filter(df.container_id == "XPOG1294738").rdd.count()

def test_ejercicio_3_resultados_guardados_formato_parquet_y_estructura_dataframe_correcta(spark_context, path_resultados):

  path = path_resultados(3)

  assert os.path.isdir(path) == True

  sqlContext = SQLContext(spark_context)

  df = sqlContext.read.parquet(path)
  
  assert df.count() == 613

  correct = ['contact', 'container_group', 'container_id', 'container_type', 'country', 'customs_ok', 'declared', 'departure', 'gross_weight', 'net_weight', 'owner', 'ship_imo', 'ship_name']
  returned = sorted([column.lower() for column in df.columns])

  assert correct == returned


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import pytest
import shutil
import sys

from glob import glob
from helpers import definir_path_resultados, comprobar_resultados_en_hdfs

spark_home = os.environ.get('SPARK_HOME', None)
if not spark_home:
  raise ValueError("Unable to find Spark, make sure SPARK_HOME environment variable is set")

if not os.path.exists(spark_home):
  raise ValueError("Cannot find path set in SPARK_HOME: " + spark_home)

spark_python = os.path.join(spark_home, 'python')
py4j = glob(os.path.join(spark_python, 'lib', 'py4j-*.zip'))[0]
sys.path[:0] = [spark_python, py4j]

from pyspark.context import SparkContext

@pytest.fixture(scope='session')
def spark_context(request):
  sc = SparkContext('local', 'tests_practicas_spark')
  request.addfinalizer(lambda: sc.stop())
  logger = logging.getLogger('py4j')
  logger.setLevel(logging.WARN)
  return sc

@pytest.fixture(scope='session')
def path_resultados(request):
  return definir_path_resultados('./resultados')

@pytest.fixture(scope='session')
def resultados_ejercicio_3(spark_context, path_resultados):
  from contenedores import ejercicio_3
  return ejercicio_3(spark_context, path_resultados)

@pytest.fixture(scope='session')
def comprobar_hdfs(path_resultados):
  def check(ejercicio_n):
    path = path_resultados(ejercicio_n)
    return comprobar_resultados_en_hdfs(path)
  return check

@pytest.fixture(scope='session')
def tiene_columnas():
  def check(df, expected):
    assert df is not None, 'El DataFrame no existe ¿Olvidaste un "return df" al final del ejercicio?'
    assert sorted(expected) == sorted([column.lower() for column in df.columns])
  return check


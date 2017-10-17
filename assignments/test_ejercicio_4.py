
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os
from pyspark.sql import SQLContext

def test_ejercicio_4_puede_filtrar_la_lista_de_contenedores(spark_context, path_resultados):
  df = ejercicio_4(spark_context, path_resultados)
  assert [row.ship_imo for row in df.rdd.collect()] == [
      u'AEY1108363', 
      u'AMC1861710',
      u'DEJ1128330',
      u'FUS1202266',
      u'GEU1548633',
      u'GLV1922612',
      u'GYR1192020',
      u'IWE1254579',
      u'JCI1797526',
      u'JET1053895',
      u'JMP1637582',
      u'KSP1096387',
      u'MBV1836745',
      u'NCZ1777367',
      u'NLH1771681',
      u'POG1615575',
      u'RYP1117603',
      u'SQH1155999',
      u'TCU1641123',
      u'YZX1455509']

def test_ejercicio_4_resultados_guardados(comprobar_hdfs):
  assert comprobar_hdfs(4) == True

def test_ejercicio_4_resultados_guardados_formato_json_y_estructura_dataframe_correcta(spark_context, path_resultados):
  sqlContext = SQLContext(spark_context)

  df = sqlContext.read.json(path)
  
  assert df.count() == 20

  correct = ['ship_imo']
  returned = [column.lower() for column in df.columns]

  assert correct == returned


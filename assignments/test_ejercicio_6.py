#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

from contenedores import *

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_6(spark_context, path_resultados)

def test_ejercicio_6_existen_261_contenedores_agrupados(resultados):
  assert 261 == resultados.rdd.count()

def test_ejercicio_6_al_menos_uno_de_los_contenedores_validos_existe_en_la_lista(resultados):
  esperados = [109383187.34, 14038620.92, 213307524.22, 26936712.06, 29567214.06, 36127305.83, 38100695.63, 57417325.75, 60934192.91, 723432237.28]
  assert sorted(esperados) == sorted([r["total_net_weight"] for r in resultados.rdd.collect() if r["ship_imo"] == u'GLV1922612'], key=float)

def test_ejercicio_6_estructura_dataframe_correcta(resultados, tiene_columnas):
  tiene_columnas(resultados, ['container_group', 'ship_imo', 'ship_name', 'total_net_weight'])


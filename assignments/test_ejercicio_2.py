#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

from contenedores import *

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_2(spark_context, path_resultados)

def test_ejercicio_2_solo_quedan_dos_contenedores_despues_de_filtrar(resultados):
  assert 2 == len(resultados)

def test_ejercicio_2_comprobar_que_las_matriculas_son_las_correctas(resultados):
  assert all([e[0] == 'DEJ1128330' for e in resultados])
  assert 'GYFD1228113' in [e[4] for e in resultados]
  assert 'MBPF1909627' in [e[4] for e in resultados]

def test_ejercicio_2_resultados_guardados(comprobar_hdfs):
  assert comprobar_hdfs(2) == True


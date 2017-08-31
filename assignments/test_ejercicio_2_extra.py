
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

import os

@pytest.fixture(scope="session")
def resultados(spark_context, path_resultados):
  return ejercicio_2(spark_context, path_resultados)

def test_ejercicio_2_resultados_guardados_formato_texto(spark_context, path_resultados, resultados):

  path = path_resultados(2)

  assert os.path.isfile(path) == True

  assert os.stat(path).st_size > 0L


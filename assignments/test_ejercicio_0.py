import pytest

from .contenedores import *

def test_ejercicio_0_crea_secuencia_de_10_elementos(spark_context, path_resultados):
  resultado = ejercicio_0(spark_context, path_resultados)
  esperado = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  assert resultado == esperado


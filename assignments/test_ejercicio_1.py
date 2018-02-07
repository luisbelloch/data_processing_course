import pytest

from contenedores import *

def test_ejercicio_1_cuenta_correctamente_el_numero_de_lineas(spark_context, path_resultados):
  resultado = ejercicio_1(spark_context, path_resultados)
  assert 614 == resultado


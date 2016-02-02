#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from contenedores import *

def test_ejercicio_2_solo_quedan_dos_contenedores_despues_de_filtrar(spark_context, path_resultados):
  resultado = ejercicio_2(spark_context, path_resultados)
  assert 2 == len(resultado)
  assert all([e[0] == 'DEJ1128330' for e in resultado])


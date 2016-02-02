#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from contenedores import *

def test_ejercicio_3_data_frame_tiene_613_filas(resultados_ejercicio_3):
  assert 613 == resultados_ejercicio_3.rdd.count()

def test_ejercicio_3_data_frame_tiene_al_menos_una_fila_correcta(resultados_ejercicio_3):
  df = resultados_ejercicio_3
  assert 1 == df.filter(df.ship_imo == "JMP1637582").filter(df.container_id == "XPOG1294738").rdd.count()



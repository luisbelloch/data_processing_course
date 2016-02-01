#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from helpers import *

sc = SparkContext('local', 'compras')
txt = sc.textFile('data/compras_tiny.csv')
no_header = txt.filter(lambda s: not s.startswith(item_fields[0]))
parsed = no_header.map(lambda s: parse_item(s)).cache()

# Primera aproximación
mas_de_un_cupon = parsed \
    .map(lambda i: (i.tx_id, i.coupon_code)) \
    .filter(lambda t: t[1]) \
    .map(lambda t: (t[0], 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .filter(lambda t: t[1] > 1)
print("Plan de ejecución (v1):") 
print(mas_de_un_cupon.toDebugString().decode('utf-8'))
print("Con más de un descuento (v1):", mas_de_un_cupon.count())

# Segunda aproximación, código equivalente
mas_de_un_cupon2 = parsed \
    .map(lambda i: (i.tx_id, 1 if i.coupon_code else 0)) \
    .filter(lambda t: t[1] == 1) \
    .reduceByKey(lambda a, b: a + b) \
    .filter(lambda t: t[1] > 1)
print("\nPlan de ejecución (v2):") 
print(mas_de_un_cupon2.toDebugString().decode('utf-8'))
print("Con más de un descuento (v2):", mas_de_un_cupon2.count())

total = parsed.count()
p_descuentos = mas_de_un_cupon2.count() / float(total)
print("Porcentaje:", p_descuentos)

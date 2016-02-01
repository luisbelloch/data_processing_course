#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from helpers import *

sc = SparkContext('local', 'compras')
txt = sc.textFile('data/compras_tiny.csv')
no_header = txt.filter(lambda s: not s.startswith(item_fields[0]))
parsed = no_header.map(lambda s: parse_item(s)).cache()

importes = parsed \
    .map(lambda i: (i.tx_id, float(i.item_price))) \
    .reduceByKey(lambda elemento, acumulado: elemento + acumulado)

print(importes.take(10))


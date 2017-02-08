#!/usr/bin/env python
from __future__ import print_function
from pyspark import SparkContext

sc = SparkContext('local', 'hello')
rdd = sc.textFile('data/compras_tiny.csv')

solo_en_euros = rdd.filter(lambda fila: 'EUR' in fila)

print(solo_en_euros.toDebugString())
print(solo_en_euros.count())
print(solo_en_euros.take(10))


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

from helpers import *

sc = SparkContext('local', 'barcos')
sq = SQLContext(sc)

# Leer archivo como CSV e inferir el esquema
# Exportar todo como archivo de parquet
csv_source = sc \
    .textFile('data/containers_tiny.csv') \
    .filter(lambda s: not s.startswith(container_fields[0])) \
    .map(parse_container) \
    .map(lambda c: Row(**dict(c._asdict())))

print(csv_source.count())

# Python 2.7.6 to 3.5 
# http://stackoverflow.com/a/26180604
# .map(lambda c: Row(**dict(c.__dict__)))

containerSchema = sq.createDataFrame(csv_source)
containerSchema.createOrReplaceTempView('container')

denmark_only = sq.sql("SELECT ship_name FROM container WHERE country = 'DK'")
print(denmark_only.first())

todo_df = sq.sql("SELECT * FROM container")
print(todo_df.printSchema())

outpath = 'data/containers_tiny.parquet'
todo_df.write.mode('overwrite').parquet(outpath)
print("\nDatos guardados en", outpath)

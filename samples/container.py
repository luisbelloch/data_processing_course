#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

from helpers import *

sc = SparkContext('local', 'barcos')
sq = SQLContext(sc)

df = sq.read.load('data/containers_tiny.parquet')
df.printSchema()

# Using API
df.select("ship_imo", "ship_name", "country").filter(df['country'] == 'DK').show()

# Register table alias to allow SQL use
df.createOrReplaceTempView("container")
sq.sql("SELECT ship_imo, ship_name FROM container WHERE country = 'DK'").show()

# ship_imo, num of containers, total ship weight
total_weight_rdd = sq.sql("SELECT ship_imo, count(container_id) number, sum(net_weight) total_weight FROM container GROUP BY ship_imo")
total_weight_rdd.printSchema()
total_weight_rdd.show()
# print total_weight_rdd.map(lambda r: r['number']).collect()

# UDFs
sq.registerFunction('en_toneladas', lambda c: float(c) / 1000.0)
sq.sql("SELECT en_toneladas(net_weight) toneladas, net_weight FROM container WHERE container_id = 'FMBV1684747'").show()

# JOINs: Extract description of container codes
codes = sq.read.json('data/iso-container-codes.json')
codes.createOrReplaceTempView('codes')
codes.printSchema()
codes.show()

w_desc = sq.sql("SELECT c.container_id, s.code, s.description FROM container c JOIN codes s on c.container_type = s.code")
w_desc.show()
print(w_desc.groupBy("code").count().take(3))


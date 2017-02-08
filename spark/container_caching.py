#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

sc = SparkContext('local', 'barcos')
sq = SQLContext(sc)

df = sq.read.load('data/containers_tiny.parquet')
df.registerTempTable("container")
sq.cacheTable("container")

df.select("ship_imo", "ship_name", "country").filter(df['country'] == 'DK').show()
sq.sql("SELECT ship_imo, ship_name FROM container WHERE country = 'DK'").show()
sq.sql("SELECT ship_imo, count(container_id) number, sum(net_weight) total_weight FROM container GROUP BY ship_imo").show()

raw_input("Press Enter to continue... http://localhost:4040/storage")


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import lead, col, explode
from pyspark.sql.window import Window

from graphframes import *
from graphframes.examples import Graphs

sc = SparkContext('local', 'barcos')
sq = SQLContext(sc)

csv = sc.textFile("data/ship_routes.csv") \
    .map(lambda c: c.split("|")) \
    .map(lambda c: (c[0], c[1], c[4]))
sequential_route = sq.createDataFrame(csv, ["order", "ship_imo", "country_code"])
sequential_route.orderBy("ship_imo", "order").show()

w = Window().partitionBy("ship_imo").orderBy(col("order"))
routes = sequential_route.select("*", lead("country_code").over(w).alias("dst")).na.drop()
routes.orderBy("ship_imo", "order").show()

edges = routes.select(col("country_code").alias("src"), col("dst"), col("ship_imo"))
# edges.show(100)

countries_rdd = sc \
    .textFile('./data/country_codes.csv') \
    .map(lambda c: tuple(reversed(c.split(','))))
vertices = sq.createDataFrame(countries_rdd, ["id", "country_label"])
# vertices.show(100)

g = GraphFrame(vertices, edges)
results = g.shortestPaths(landmarks=["AT", "GS"]) \
           .select("id", "country_label", explode("distances"))
results.show(200)


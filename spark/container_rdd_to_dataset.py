#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

csv_source = spark.sparkContext \
    .textFile('data/containers_tiny.csv') \
    .filter(lambda s: not s.startswith("ship_imo")) \
    .map(lambda i: i.split(";")) \
    .map(lambda i: (i[4], i[5], float(i[7]))) \
    .cache()

print(csv_source.take(1))

# Set schema 
container_id_field = StructField("container_id", StringType(), True) 
container_type_field = StructField("container_type", StringType(), True) 
net_weight_field = StructField("net_weight", FloatType(), True) 
schemaDef = StructType([container_id_field, container_type_field, net_weight_field])

schema = spark.createDataFrame(csv_source, schemaDef)
schema.printSchema()


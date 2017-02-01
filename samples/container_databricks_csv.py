#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

# https://github.com/databricks/spark-csv#python-api
df = spark.read \
    .format("com.databricks.spark.csv") \
    .options(header='true', inferschema='true', delimiter=";") \
    .load('data/containers_tiny.csv')

df.printSchema()
df.show()

df.select("container_id", "container_type", "gross_weight") \
  .filter(df["country"] == "DK") \
  .show()

df.groupBy("country").count().show()

df.createOrReplaceTempView("container")
spark.sql("SELECT ship_name FROM container WHERE country = 'DK'").show()




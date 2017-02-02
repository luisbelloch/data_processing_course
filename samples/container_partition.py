#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark.sql import SparkSession

from helpers import *

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

df = spark.read.load('data/containers_tiny.parquet')

def segment(field, value, num = 5):
    df.filter(df[field] == value).limit(num) \
        .write.mode('overwrite') \
        .parquet('data/containers_partitioned/{}={}'.format(field, value))

segment("country", "DK")
segment("country", "SB")

for path, dirs, files in os.walk('data/containers_partitioned/'):
    print("\x1b[38;5;214m"+path+"\033[0m")
    for f in files:
        print("  |-- ", f)

partitioned = spark.read.load("data/containers_partitioned")
partitioned.select("container_id", "country").show()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from os import walk

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

def segment(df, field, value, num = 5):
  df.filter(df[field] == value).limit(num) \
    .write.mode('overwrite') \
    .parquet('data/containers_partitioned/{}={}'.format(field, value))

def main():
  df = spark.read.load('data/containers_tiny.parquet')
  segment(df, "country", "DK")
  segment(df, "country", "SB")

  for path, dirs, files in walk('data/containers_partitioned/'):
    print("\x1b[38;5;214m"+path+"\033[0m")
    for f in files:
      print("  |-- ", f)
  
  partitioned = spark.read.load("data/containers_partitioned")
  partitioned.select("container_id", "country").show()

if __name__ == '__main__':
  main()


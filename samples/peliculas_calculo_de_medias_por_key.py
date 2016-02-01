#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pyspark import SparkContext
from helpers import *

sc = SparkContext('local', 'compras')

ratings = sc.textFile("data/ratings.csv") \
    .filter(lambda l: not l.startswith('pelicula_id')) \
    .map(lambda l: l.split(","))

media_ratings = ratings \
    .map(lambda r: (r[0], (float(r[2]), 1))) \
    .reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1])) \
    .map(lambda p: (int(p[0]), p[1][0] / float(p[1][1])))

print(media_ratings.take(5))


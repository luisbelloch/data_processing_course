#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.ml.recommendation import ALS
# from pyspark.mllib.evaluation import RegressionMetrics, RankingMetrics
# from pyspark.mllib.recommendation import ALS, Rating

sc = SparkContext('local', 'peliculas')
sq = SQLContext(sc)

df = sq.createDataFrame([(0, 0, 4.0), (0, 1, 2.0), (1, 1, 3.0), (1, 2, 4.0), (2, 1, 1.0), (2, 2, 5.0)], ["user", "item", "rating"])
df.show()

als = ALS()
model = als.fit(df)

test = sq.createDataFrame([(0, 2), (1, 0), (2, 0), (3, 0)], ["user", "item"])
model.transform(test).show()


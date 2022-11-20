from os import walk

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

df = spark.read.option("delimiter", "|").option("header", "true").csv('./data/compras_tiny.csv')
df.printSchema()
df.show()

df.createOrReplaceTempView("compras")
spark.sql("SELECT tx_id, SUM(item_price) as tx_total FROM compras GROUP BY tx_id").show()

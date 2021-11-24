from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()
df = spark.read.load('data/containers_tiny.parquet')
df.select("ship_imo", "container_id", "net_weight").show()


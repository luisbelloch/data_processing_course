from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("container").getOrCreate()

df = spark.read.load('data/containers_tiny.parquet')
df.printSchema()

# Using API
df.select("ship_imo", "ship_name", "country").filter(df['country'] == 'DK').show()

# Register table alias to allow SQL use
df.createOrReplaceTempView("container")
spark.sql("SELECT ship_imo, ship_name FROM container WHERE country = 'DK'").show()

# ship_imo, num of containers, total ship weight
total_weight_rdd = spark.sql("SELECT ship_imo, count(container_id) number, sum(net_weight) total_weight FROM container GROUP BY ship_imo")
total_weight_rdd.printSchema()
total_weight_rdd.show()
# print total_weight_rdd.map(lambda r: r['number']).collect()

# UDFs
spark.udf.register('en_toneladas', lambda c: float(c) / 1000.0)
spark.sql("SELECT en_toneladas(net_weight) toneladas, net_weight FROM container WHERE container_id = 'FMBV1684747'").show()

# JOINs: Extract description of container codes
codes = spark.read.json('data/iso-container-codes.json')
codes.createOrReplaceTempView('codes')
codes.printSchema()
codes.show()

w_desc = spark.sql("SELECT c.container_id, s.code, s.description FROM container c JOIN codes s on c.container_type = s.code")
w_desc.show()
print(w_desc.groupBy("code").count().take(3))


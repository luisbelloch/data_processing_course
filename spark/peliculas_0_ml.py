from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

# ALTERNATIVE
# from pyspark.mllib.evaluation import RegressionMetrics, RankingMetrics
# from pyspark.mllib.recommendation import ALS, Rating

spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

print("\033[36mInitial data\033[0m")
columns = ["user", "item", "rating"]
data = [(0, 0, 4.0), (0, 1, 2.0), (1, 1, 3.0), (1, 2, 4.0), (2, 1, 1.0), (2, 2, 5.0)]
df = spark.createDataFrame(data, columns)
df.show()

print("\033[36mTraining model...\033[0m")
als = ALS()
model = als.fit(df)

output_model_path = "data/peliculas0_trained_model"
print("\033[36mSaving model to '{}'...\033[0m".format(output_model_path))
model.write().overwrite().save(output_model_path)

print("\033[36mTesting some user/item pairs...:\033[0m")
test = spark.createDataFrame([(0, 2), (1, 0), (2, 0), (3, 0)], ["user", "item"])
model.transform(test).show()


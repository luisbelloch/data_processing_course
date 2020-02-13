from pyspark import SparkContext

sc = SparkContext('local', 'hello')
rdd = sc.textFile('./data/compras_tiny.csv')

print(rdd.count())

# Also spark-submit hello1.py --conf spark.logLineage=true
print(rdd.toDebugString().decode('utf-8'))


import sys
from pyspark import SparkContext
from helpers import dataUrl, item_fields, parse_item

sc = SparkContext('local', 'compras')
txt = sc.textFile(dataUrl('compras_tiny.csv'))
no_header = txt.filter(lambda s: not s.startswith(item_fields[0]))
parsed = no_header.map(lambda s: parse_item(s)).cache()

countries_rdd = sc \
    .textFile(dataUrl('country_codes.csv')) \
    .map(lambda c: tuple(reversed(c.split(','))))

join_rdd = parsed \
    .filter(lambda i: i.currency_code == 'USD') \
    .map(lambda i: (i.country, float(i.item_price))) \
    .reduceByKey(lambda a, b: a + b) \
    .leftOuterJoin(countries_rdd) \
    .sortBy(lambda i: i[1][0], ascending=False)

print(join_rdd.take(10))

# print map(lambda i: (i[0], i[1][1], i[1][0]), join_rdd.take(10))
# join_rdd.saveAsTextFile(dataUrl('out/top10countries'), 'org.apache.hadoop.io.compress.GzipCodec')


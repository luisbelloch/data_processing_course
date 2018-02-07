# RUN: ./graphframes.sh ship_routes.py

from pyspark import SparkContext
from pyspark.sql import SQLContext

from graphframes import *
from graphframes.examples import Graphs

sc = SparkContext('local', 'friends')
sq = SQLContext(sc)
friends = Graphs(sq).friends()

friends.vertices.show()
friends.edges.show()

over30 = friends.vertices.filter("age > 30")
only_friends = friends.edges.filter("relationship = 'friend'")
friends_over_30 = GraphFrame(over30, only_friends)
friends_over_30.triplets.show()


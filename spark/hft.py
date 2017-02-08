#!/usr/bin/env python

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from helpers import *

sc = SparkContext("local[2]", "NetworkWordCount")
st = StreamingContext(sc, 1)
setup_checkpoint(st)

portfolio = { u'MSFT': Stock('MSFT', 1, 150.06, None, 0.0), u'APPL': Stock('APPL', 4, 70.23, None, 0.0), u'GOOG': Stock('GOOG', 2, 104.55, None, 0.0) }

def actualizar_portfolio(stocks):
    actualizaciones = stocks.filter(lambda s: s.simbolo in portfolio).collect()
    al_menos_una_actualizacion = False
    for a in actualizaciones:
        al_menos_una_actualizacion = True
        actual = portfolio[a.simbolo]
        nuevo = actual._replace( \
            ultimo_precio = a.ultimo_precio, \
            returns = (a.ultimo_precio - actual.precio_compra) / actual.precio_compra)
        portfolio[a.simbolo] = nuevo
    if al_menos_una_actualizacion:
        print map(lambda s: list(s), portfolio.values())

stocks = st.socketTextStream("localhost", 9999) \
    .map(parse_stock) \
    .foreachRDD(actualizar_portfolio)

# stocks.pprint()
# stocks.reduceByKey(lambda a,b: a + b)

st.start()
st.awaitTermination()


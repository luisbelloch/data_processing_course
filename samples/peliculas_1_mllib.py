#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark import SparkContext
from pyspark.mllib.evaluation import RegressionMetrics, RankingMetrics
from pyspark.mllib.recommendation import ALS, Rating

sc = SparkContext()

# Generar recomendaciones para todos los usuarios
# - Clasificación: suma(votos) / numero_votos
# - Clasificación con tiempo: inventar, algoritmo de Reddit p.e.
# - Descartar votos duplicados
# - Report para la web, necesario orden por pelicula: usuario_id, pelicula_id, titulo, rating_medio
# - Guardar en parquet

peliculas = sc.textFile("data/peliculas.csv") \
    .filter(lambda l: not l.startswith(u'#') and not l.startswith(u'Entry|')) \
    .map(lambda l: l.split("|"))
# print peliculas.take(2)

def parseLine(line):
    fields = line.split("|")
    return Rating(int(fields[0]), int(fields[1]), float(fields[2]) - 2.5)

ratings = sc.textFile("data/ratings.csv") \
    .filter(lambda l: not l.startswith('pelicula_id')) \
    .map(lambda l: l.split(",")) \
    .map(lambda l: Rating(int(l[1]), int(l[0]), float(l[2])))
# print ratings.take(2)

media_ratings = ratings \
    .map(lambda r: (r.product, (r.rating, 1))) \
    .reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1])) \
    .map(lambda p: (p[0], p[1][0] / float(p[1][1])))
# print media_ratings.collect()

# Entrenar modelo
model = ALS.train(ratings, 1)

# generar posibles pares de usuario / pelicula
# VER bash en shell_trans.sh
ids_pelicula = sc.textFile('data/pelicula_ids.csv')
ids_usuario = sc.textFile('data/pelicula_usuarios.csv')
publico_objetivo = ids_usuario.cartesian(ids_pelicula)  #ids_pelicula.cartesian(ids_usuario)
# print posibles_pares.take(10)

# Crear predicciones
predicciones = model.predictAll(publico_objetivo)
# print predicciones.take(4)

# Convertir a DF para manipular
# POR QUÉ no hemos de hacer el sort/join aquí, mejor en una BBDD relacional
# Cálculo número de filas + espacio
# Cómo se realizaría la inserción?
from pyspark.sql import SQLContext, Row
sq = SQLContext(sc)
df = sq.createDataFrame(predicciones)
df.registerTempTable('predicciones')
df.show()

# ¿Tenemos un modelo correcto?
# R-Squared 0, indicates that the model explains none of the variability of the response data around its mean.
# R-Squared 1, indicates that the model explains all the variability of the response data around its mean.
ratingsTuple = ratings.map(lambda r: ((r.user, r.product), r.rating))
scoreAndLabels = predicciones \
        .map(lambda r: ((r.user, r.product), r.rating)) \
        .join(ratingsTuple) \
        .map(lambda tup: tup[1])

metrics = RegressionMetrics(scoreAndLabels)
print("RMSE = %s" % metrics.rootMeanSquaredError)
print("R-squared = %s" % metrics.r2)

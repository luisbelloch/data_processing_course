#!/usr/bin/env python
from __future__ import absolute_import

import datetime
import logging

import apache_beam as beam

logging.getLogger().setLevel(logging.INFO)

def dump(line):
  logging.info(line)
  return line

def isoDate(date):
  return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

@beam.ptransform_fn
def ParseCompras(pcol):
  return (pcol
    | 'SplitFields' >> beam.Map(lambda l: l.split("|"))
    | 'SkipHeader' >> beam.Filter(lambda l: l[0] != 'tx_id')
    | 'Struct' >> beam.Map(lambda f: (f[3], float(f[9]))))

p = beam.Pipeline()
compras = (p
  | beam.io.ReadFromText("/data/compras_tiny.csv")
  | ParseCompras())

totales = (compras | beam.CombinePerKey(sum))
cuentas = (compras | beam.combiners.Count.PerKey())

({ "total": totales, "cuenta": cuentas} 
  | 'Join' >> beam.CoGroupByKey()
  | 'Flatten' >> beam.Map(lambda e: "%s|%f|%d" % (e[0], e[1]["total"][0], e[1]["cuenta"][0]))
  | 'Dump' >> beam.Map(lambda x: dump(x))
  | 'Write' >> beam.io.WriteToText('/data/compras_totales_por_pais'))

p.run().wait_until_finish()


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

p1 = beam.Pipeline()
lines_collection = (p1
  | 'LecturaCompras' >> beam.io.ReadFromText("/data/compras_tiny.csv")
  | 'Split' >> beam.Map(lambda l: l.split("|"))
  | 'SkipHeader' >> beam.Filter(lambda l: l[0] != 'tx_id')
  | 'DosCampos' >> beam.Map(lambda f: { "tx_id": f[0], "tx_time": isoDate(f[1]) })
  | 'DebugPrint' >> beam.Map(lambda x: dump(x)))

p1.run().wait_until_finish()


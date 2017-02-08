#!/usr/bin/env python
from __future__ import absolute_import

import datetime
import logging

import apache_beam as beam

# ./beam compras_ptransform.py
# head ../data/compras_tiny.json/compras_tiny.json-00000-of-00018
# {'tx_id': u'RHMLNJB157', 'tx_time': datetime.datetime(2010, 2, 3, 4, 12, 3)}
# {'tx_id': u'VFJDQNX118', 'tx_time': datetime.datetime(2010, 10, 24, 3, 1, 9)}
# {'tx_id': u'MYOIBZV163', 'tx_time': datetime.datetime(2010, 7, 26, 5, 23, 35)}

logging.getLogger().setLevel(logging.INFO)

def dump(line):
  logging.info(line)
  return line

def isoDate(date):
  return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

class ParseCompras(beam.PTransform):
  def init(self):
    super(ParseCompras, self).__init__()

  def expand(self, pcol):
    return (pcol
      | 'SplitFields' >> beam.Map(lambda l: l.split("|"))
      | 'SkipHeader' >> beam.Filter(lambda l: l[0] != 'tx_id')
      | 'DosCampos' >> beam.Map(lambda f: { "tx_id": f[0], "tx_time": isoDate(f[1]) }))

p1 = beam.Pipeline()
lines_collection = (p1
  | 'LecturaCompras' >> beam.io.ReadFromText("/data/compras_tiny.csv")
  | ParseCompras()
  # | 'DebugPrint' >> beam.Map(lambda x: dump(x))
  | 'Write' >> beam.io.WriteToText('/data/compras_tiny.json/compras_tiny.json'))

p1.run().wait_until_finish()


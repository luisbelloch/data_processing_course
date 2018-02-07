import json
import os
import shutil

from collections import namedtuple
from datetime import datetime

item_fields = ['tx_id', 'tx_time', 'buyer', 'currency_code', 'payment_type', 'credit_card_number', 'country', 'department', 'product', 'item_price', 'coupon_code', 'was_returned']
Item = namedtuple('Item', item_fields)

def parse_item(raw_string):
  f = raw_string.split('|')
  f += [None] * (len(item_fields) - len(f))
  return Item(*f)

# Uso básico de namedtuples:
# Thing = namedtuple('Item', ['foo', 'bar'])
# some = Thing(foo=42, bar='hello')
# some.foo
# item = parse_item(["one", "two"])
# new_item = item._replace(tx_id=1, buyer=5)

# API http://fixer.io/
def get_usd_exchange_rates():
  with open('./data/exchange_rates_usd.json') as f:
    data = json.load(f)
    return data['rates']

container_fields = ['ship_imo', 'ship_name', 'country', 'departure', 'container_id', 'container_type', 'container_group', 'net_weight', 'gross_weight', 'owner', 'declared', 'contact', 'customs_ok']
Container = namedtuple('Container', container_fields)

def parse_container(raw_string):
  f = raw_string.split(';')
  f += [None] * (len(container_fields) - len(f))
  return Container(*f)

stock_fields = ['simbolo', 'numero', 'precio_compra', 'ultimo_precio', 'returns']
Stock = namedtuple('Stock', stock_fields)
def parse_stock(raw_string):
  f = raw_string.split(',')
  return Stock(simbolo=f[0], numero=None, precio_compra=None, ultimo_precio=float(f[1]), returns=0.0)

def setup_checkpoint(streamingContext):
  checkpoint = './checkpoint'
  if (os.path.exists(checkpoint)):
    shutil.rmtree(checkpoint)
  os.mkdir(checkpoint)
  streamingContext.checkpoint(checkpoint)

def isoDate(raw_string):
  try:
    return datetime.strptime(raw_string, "%Y-%m-%dT%H:%M:%SZ")
  except Exception:
    return None


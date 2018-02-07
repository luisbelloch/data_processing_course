from pyspark import SparkContext
from helpers import get_usd_exchange_rates, item_fields, parse_item

sc = SparkContext('local', 'compras')
txt = sc.textFile('data/compras_tiny.csv')
no_header = txt.filter(lambda s: not s.startswith(item_fields[0]))
parsed = no_header.map(lambda s: parse_item(s)).cache()

rates = get_usd_exchange_rates()

# El archivo puede tener múltiples problemas, incluso con algo 
# sencillo como una simple conversion a dólares:
# - el precio ya está en dólares
# - item_price no viene como float
# - no existe tasa de cambio para ese item
# - ¿Cómo descartamos la linea? -> None
# - ¿Cómo recogemos las filas que han fallado? ¿debemos?
def convert_to_usd(item):
    if (item.currency_code == 'USD'):
        return item
    if (not item.currency_code in rates):
        return None # error?
    new_price = rates[item.currency_code] * float(item.item_price)
    new_item = item._replace(currency_code='USD', item_price = new_price)
    return new_item

in_usd = parsed.map(convert_to_usd)
print(in_usd.take(2))


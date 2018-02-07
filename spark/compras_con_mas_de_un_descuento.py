from pyspark import SparkContext
from helpers import parse_item, item_fields

sc = SparkContext('local', 'compras')
txt = sc.textFile('data/compras_tiny.csv')
no_header = txt.filter(lambda s: not s.startswith(item_fields[0]))
parsed = no_header.map(lambda s: parse_item(s)).cache()

# Brief talk on why color in terminal should not be abused, logs get destroyed

# Primera aproximación
mas_de_un_cupon = parsed \
    .map(lambda i: (i.tx_id, i.coupon_code)) \
    .filter(lambda t: t[1]) \
    .map(lambda t: (t[0], 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .filter(lambda t: t[1] > 1)
print("\033[35mPlan de ejecución (v1):\033[0m") 
print(mas_de_un_cupon.toDebugString().decode('utf-8'))
print("\033[35mCon más de un descuento (v1):\033[0m", mas_de_un_cupon.count())

# Segunda aproximación, código equivalente
mas_de_un_cupon2 = parsed \
    .map(lambda i: (i.tx_id, 1 if i.coupon_code else 0)) \
    .filter(lambda t: t[1] == 1) \
    .reduceByKey(lambda a, b: a + b) \
    .filter(lambda t: t[1] > 1)
print("\n\033[36mPlan de ejecución (v2):\033[0m") 
print(mas_de_un_cupon2.toDebugString().decode('utf-8'))
print("\033[36mCon más de un descuento (v2):\033[0m", mas_de_un_cupon2.count())

total = parsed.count()
p_descuentos = mas_de_un_cupon2.count() / float(total)
print("\n\x1b[38;5;214mPorcentaje:\x1b[0m", p_descuentos, "\n")


from pyspark import SparkContext
from pyspark.sql import SQLContext, Row

from .helpers import *

path_containers = 'data/containers.csv'

def ejercicio_0(sc, path_resultados):
  lineas = sc.parallelize(range(10)).collect()
  with open(path_resultados(0), 'w') as f:
    f.write("{}\n".format(",".join([str(s) for s in lineas])))
  return lineas

# Ejercicio 1. Leer el archivo data/containers.csv y contar el número de líneas.
def ejercicio_1(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Devolver número de líneas
  return 0

# Ejercicio 2. Leer el archivo data/containers.csv y filtrar aquellos
# contenedores cuyo ship_imo es DEJ1128330 y el grupo del contenedor es 22P1.
# Guardar los resultados en un archivo de texto en resultados/resutado_2.
def ejercicio_2(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar en resultados/resultado_2. La función path_resultados devuelve
  # la ruta donde se van a guardar los resultados, para que los tests puedan
  # ejecutar de forma correcta. Por ejemplo, path_resultados(2) devuelve la
  # ruta para el ejercicio 2, path_resultados(3) para el 3, etc.
  # Devolver rdd contenedores filtrados:
  # return rdd.collect()
  pass

# Ejercicio 3. Leer el archivo data/containers.csv y convertir a formato
# Parquet. Recuerda que puedes hacer uso de la funcion parse_container en
# helpers.py tal y como vimos en clase. Guarda los resultados en
# resultados/resultado_3.
def ejercicio_3(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar resultados y devolver DataFrame (return df)
  pass

# Ejercicio 4. Lee el archivo de Parquet guardado en el ejercicio 3 y filtra
# los barcos que tienen al menos un contenedor donde la columna customs_ok es
# igual a false. Extrae un fichero de texto una lista con los identificadores
# de barco, ship_imo, sin duplicados y ordenados alfabéticamente.
def ejercicio_4(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar resultados y devolver DataFrame (return df)
  pass

# Ejercicio 5. Crea una UDF para validar el código de identificación del
# contenedor container_id. Para simplificar la validación, daremos como
# válidos aquellos códigos compuestos de 3 letras para el propietario, 1
# letra para la categoría, 6 números y 1 dígito de control. Devuelve un
# DataFrame con los campos: ship_imo, container_id, propietario, categoria,
# numero_serie y digito_control.
def ejercicio_5(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar resultados y devolver DataFrame (return df)
  pass

# Ejercicio 6. Extrae una lista con peso total de cada barco, `net_weight`,
# sumando cada contenedor y agrupado por los campos `ship_imo` y `container_group`.
# Devuelve un DataFrame con la siguiente estructura:
# `ship_imo`, `ship_name`, `container_group`, `total_net_weight`.
def ejercicio_6(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar resultados y devolver DataFrame (return df)
  pass

# Ejercicio 7. Guarda los resultados del ejercicio anterior en formato Parquet.
def ejercicio_7(sc, path_resultados):
  # COMPLETAR CÓDIGO AQUÍ
  # Guardar resultados y devolver DataFrame (return df)
  pass

def main():
  sc = SparkContext('local', 'practicas_spark')
  pr = definir_path_resultados('./resultados')
  ejercicio_0(sc, pr)
  ejercicio_1(sc, pr)
  ejercicio_2(sc, pr)
  ejercicio_3(sc, pr)
  ejercicio_4(sc, pr)
  ejercicio_5(sc, pr)
  ejercicio_6(sc, pr)
  ejercicio_7(sc, pr)

if __name__ == '__main__':
  main()


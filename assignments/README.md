# Prácticas SPARK

Las prácticas consisten en desarrollar una serie de ejercicios de procesado de datos con `PySpark`.

Para completar las prácticas debe completarse un archivo llamado `contenedores.py` con los ejercicios abajo descritos. No es necesaria explicación alguna, únicamente se pide que el código esté limpio, bien estructurado y ejecute correctamente.

Los archivos de datos vienen incluidos en este repositorio en la carpeta `data`. Entre los archivos de la práctica se ha incluido [un contenedor de Docker](https://hub.docker.com/r/luisbelloch/spark-assignments/) con todo lo necesario instalado. También se ha incluido una [batería de pruebas](pruebas) para que puedas comprobar los resultados antes de entregar la práctica.

Cada ejercicio produce un resultado distinto. Los resultados deben guardarse en una carpeta denominada `resultados`, teniendo un único archivo por ejercicio con la nomenclatura `resultado_1`, `resultado_2` etc. La función `path_resultados` devuelve la ruta completa que puedes usar para guardar los datos procesados en cada ejercicio. En la mayoría de los casos debes devolver un DataFrame:

```
def ejercicio_3(sc, path_resultados):
  df = sq.sql(...)
  # ... otras operaciones
  # ... save(path_resultados(3))
  return df
```

Los ejercicios se realizarán sobre un fichero en formato CSV que contiene una lista de barcos, identificados por la columna `ship_imo`. A su vez, cada barco tiene una lista de contenedores identificados por la columna `container_id`.

Para el procesado del archivo puedes utilizar cualquier función disponible en el API de Python de Spark 2.2.1

## Plazo de entrega

Los ejercicios hay que enviarlos antes del 1 de Junio.

## Criterios de evaluación

1. El alumno entiende y es capaz de ejecutar programas en PySpark, haciendo uso de el core de Spark 2.2 y Spark SQL.
2. El archivo `contenedores.py` producido por el alumno se puede ejecutar con `spark-submit` y, opcionalmente, con `pytest`.
3. El código está estructurado correctamente, es legible y tiene una intencionalidad clara.

## Ejercicios

**Ejercicio 0**. Ejecutar el archivo `contenedores.py` y comprobar que se crea un archivo dentro de la carpeta `resultados` con números del 0 al 9.

```
$ spark-submit contenedores.py
$ cat resultados/resultado_0
0,1,2,3,4,5,6,7,8,9
```

**Ejercicio 1**. Leer el archivo `data/containers.csv` y contar el número de líneas.

**Ejercicio 2**. Leer el archivo `data/containers.csv` y filtrar aquellos contenedores cuyo `ship_imo` es `DEJ1128330` y el grupo del contenedor es `22P1`. Guardar los resultados en un archivo de texto en `resultados/resutado_2`.

**Ejercicio 3**. Leer el archivo `data/containers.csv` y convertir a formato Parquet. Recuerda que puedes hacer uso de la funcion `parse_container` en `helpers.py` tal y como vimos en clase. Guarda los resultados en `resultados/resultado_3`.

**Ejercicio 4**. Lee el archivo de Parquet guardado en el ejercicio 3 y filtra los barcos que tienen al menos un contenedor donde la columna `customs_ok` es igual a `false`. Extrae una lista con los identificadores de barco, `ship_imo`, sin duplicados y ordenados alfabéticamente, en formato `json`.

**Ejercicio 5**. Crea una UDF para validar el [código de identificación](https://en.wikipedia.org/wiki/ISO_6346) del contenedor `container_id`. Para simplificar la validación, daremos como válidos aquellos códigos compuestos de 3 letras para el propietario, 1 letra para la categoría, 6 números y 1 dígito de control. Devuelve un `DataFrame` con los campos: `ship_imo`, `container_id`, `propietario`, `categoria`, `numero_serie` y `digito_control`.

**Ejercicio 6**. Extrae una lista con peso total de cada barco, `net_weight`, sumando cada contenedor y agrupado por los campos `ship_imo` y `container_group`. Devuelve un DataFrame con la siguiente estructura: `ship_imo`, `ship_name`, `container`, `total_net_weight`.

**Ejercicio 7**. Guarda los resultados del ejercicio anterior en formato Parquet.

**Ejercicio 8**. ¿En qué casos crees que es más eficiente utilizar formatos como Parquet? ¿Existe alguna desventaja frente a formatos de texto como CSV?

**Ejercicio 9**. ¿Es posible procesar XML mediante Spark? ¿Existe alguna restricción por la cual no sea eficiente procesar un único archivo en multiples nodos? ¿Se te ocurre alguna posible solución para _trocear_ archivos suficientemente grandes? ¿Existe la misma problemática con otros formatos de texto como JSON?

**Ejercicio 10**. Spark SQL tiene [una función](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.functions.avg) denominada `avg` que se utiliza para calcular el promedio de un conjunto de valores ¿Por qué los autores han creado esta función en lugar de usar el API estándar de Python o Scala?

## Pruebas

Existe una batería de pruebas para comprobar los resultados de cada ejercicio, desarrollada sobre [pytest](http://pytest.org). Las pruebas no son exhaustivas y únicamente están orientadas a verificar los resultados de cada ejercicio. No es necesario que las pruebas pasen para entregar la práctica, aunque se valorará de forma positiva. Se deja como ejercicio optativo adaptar o ampliar la batería de pruebas.

### Ejecución de pruebas en Docker

De forma alternativa, hemos incluido una imágen de Docker con todas las dependencias necesarias. El directorio actual se montará como volumen dentro del contenedor, concretamente en `/opt/tests/assigments`.

```
$ ./test.sh
```

También es posible lanzar `bash` o `pyspark` para hacer comprobaciones manualmente:

```
$ docker run -v $(PWD):/opt/tests/assigments -ti luisbelloch/spark-assignments /bin/bash
```

### Ejecución local de pruebas

Teniendo Spark instalado mediante `local_setup.sh`, puedes instalar `pytest` en local mediante `venv`:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ export SPARK_HOME=$(pwd)/../.spark
```

Y a partir de aquí puede ejecutarse la suite de pruebas:

```
$ pytest -v
```

Para ejecutar un único test añade el nombre al final, lo único que hay que tener en cuenta es que algunos ejercicios dependen de los datos de los anteriores:

```
$ pytest -v test_ejercicio_2.py
```

Happy hacking!

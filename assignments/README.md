# Prácticas SPARK

Las prácticas consisten en desarrollar una serie de ejercicios de procesado de datos con `PySpark`. Los archivos de datos y la estructura básica de las prácticas puede descargarse en Poliformat. Entre los archivos de la práctica se ha incluido una máquina de `Vagrant` con todo lo necesario instalado.

Para completar el ejercicio debe enviarse un único archivo llamado `contenedores.py`.

Cada ejercicio produce un resultado distinto. Los resultados deben guardarse en una carpeta denominada `resultados`, teniendo un único archivo de resultados por ejercicio con la nomenclatura `resultado_1`, `resultado_2` etc.

Hemos incluido los archivos de datos esperados en la carpeta `soluciones` para que puedas comprobar los mismos antes de enviar el ejercicio. Algunos ejercicios no escriben a disco y especifican devolver directamente el `DataFrame` o el `RDD` según corresponda.

Los ejercicios se realizarán sobre un fichero en formato CSV que contiene una lista de barcos, identificados por la columna `ship_imo`. A su vez, cada barco tiene una lista de contenedores identificados por la columna `container_id`.

Para el procesado del archivo puedes utilizar cualquier función disponible en el API de Python de Spark 1.6, así como Spark SQL cuando lo consideres conveniente.

## Plazo de entrega

Los ejercicios hay que enviarlos antes del 1 de agosto.

## Criterios de evaluación

1. El alumno entiende y es capaz de ejecutar programas en PySpark, haciendo uso de el core de Spark 1.6 y Spark SQL.
2. El archivo `contenedores.py` producido por el alumno se puede ejecutar con `spark-submit` y, opcionalmente, con `py.test`.
3. Los resultados producidos coinciden con los de la carpeta `soluciones`.
4. El código está estructurado correctamente, es legible y tiene una intencionalidad clara.

## Ejercicios

**Ejercicio 0**. Ejecutar el archivo `contenedores.py` y comprobar que se crea un archivo dentro de la carpeta `resultados` con números del 0 al 9.

```
$ spark-submit contenedores.py
$ cat resultados/resultado_0
0,1,2,3,4,5,6,7,8,9
```

También puede ejecutarse la suite de pruebas mediante `py.test`, tal y como se describe [al final de este documento](pruebas). No es necesario para la entrega del ejercicio, pero puede ayudaros a comprobar los resultados de cada paso.

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

Existe una batería de pruebas para comprobar los resultados de cada ejercicio, desarrollada sobre `py.test`. Las pruebas no son exhaustivas y únicamente están orientadas a verificar los resultados de cada ejercicio. No es necesario que las pruebas pasen para entregar la práctica, aunque se valorará de forma positiva. Se deja como ejercicio optativo adaptar o ampliar la batería de pruebas. 

En la configuración de `Vagrant` de la práctica se incluye la instalación de `py.test`.

También puedes instalar `py.test` en local mediante `virtualenv`:

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export SPARK_HOME=$(pwd)/../.spark
```

A partir de aquí puede ejecutarse la suite de pruebas:

```
$ py.test -v
```

Para ejecutar un único test añade el nombre al final:

```
$ py.test -v test_ejercicio_2.py
```

Happy hacking!

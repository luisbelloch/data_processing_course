# Tutorial Dataproc (Spark)

Datapro es la versión gestionada de Spark en Google Cloud. En este tutorial vamos a cubrir como subir archivos a Cloud Storage (S3) y lanzar un trabajo de Spark para procesarlo.

Duración estimada: <walkthrough-tutorial-duration duration="45"></walkthrough-tutorial-duration>

## Preparación

### 1. Habilita las APIs necesarias

Antes de continuar es necesario habilitar las APIs de Cloud Storage y Dataproc.

<walkthrough-enable-apis apis="dataproc.googleapis.com,storage.googleapis.com ">Habilitar APIs</walkthrough-enable-apis>

### 2. Selecciona un proyecto

<walkthrough-project-setup></walkthrough-project-setup>

### 3. Abre una terminal

La mayoría de los comandos pueden ejecutarse desde la interfaz de usuario, pero en el tutorial utilizaremos la consola de cloudshell.

Si no esta abierta ya en la parte inferior puedes abrirla mediante el icono <walkthrough-cloud-shell-icon></walkthrough-cloud-shell-icon>
arriba a la derecha, o utilizando el siguiente enlace:

<walkthrough-open-cloud-shell-button></walkthrough-open-cloud-shell-button>

### 3. Materiales de clase

Asegurate de que la carpeta `cloudshell_open/data_processing_course` se ha creado. Sino, puedes abrir de nuevo el proyecto desde [bigdata.luisbelloch.es](http://bigdata.luisbelloch.es) y seleccionando [Open in Cloud Shell](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/luisbelloch/data_processing_course.git).

Alternativamente puedes clonar el repositorio mediante `git`:

```sh
git clone https://github.com/luisbelloch/data_processing_course.git && cd data_processing_course
```

## Paso 1: Crear un bucket en cloud storage

EL bucket se puede también crear desde [la UI de Google Cloud Storage](https://cloud.google.com/storage/docs/creating-buckets).

En nuestro caso podemos usar la terminal para crearlo:

```sh
gsutil mb -c regional -l europe-west1 gs://NOMBRE_BUCKET
```

Para copiar datos puede utilizarse tambien `gsutil` con `cp`:

```sh
gsutil cp data/compras_tiny.csv gs://NOMBRE_BUCKET
```

En el caso de que queramos sincronizar un directorio entero, podemos utilizar `rsync`:

```sh
gsutil -m rsync data/ gs://NOMBRE_BUCKET
```

## Paso 2: Crear un cluster en Dataproc

Lo primero que debemos hacer es crear un cluster de Spark. Para las pruebas usaremos un único nodo, pero es posible crear varios también. En nuestro caso, vamos a crear un cluster llamado `dataproc1`.

```sh
gcloud dataproc clusters create dataproc1 --region europe-west1 --single-node --enable-component-gateway
```

Una vez esté creado, podemos ver el estado del cluster en la [interfaz de usuario de Dataproc](https://console.cloud.google.com/dataproc/clusters).

Es interesante ver que Dataproc ha creado distintas máquinas virtuales [en Compute Engine](https://console.cloud.google.com/compute/instances).

<walkthrough-footnote>Recuerda eliminar el cluster al finalizar el tutorial.</walkthrough-footnote>

## Paso 3: Crear un trabajo de ejemplo de Spark

Como ejemplo, vamos a crear un script que cuente las lineas de el archivo `compras_tiny.csv`, llamado `prueba_dataproc.py`.

```python
from os import path
from pyspark import SparkContext

sc = SparkContext('local', 'hello')
rdd = sc.textFile('gs://bigdataupv_data/compras_tiny.csv')

print("Count:", rdd.count())
```

Puedes crear el script en cualquier carpeta, pero asegurate de especificar la ruta al ejecutar el trabajo en el paso siguiente.

## Paso 4: Ejecutar el trabajo de Spark

Para ejecutar el script `prueba_dataproc.py` que acabamos de crear es necesario enviarlo al cluster:

```sh
gcloud dataproc jobs submit pyspark prueba_dataproc.py --cluster dataproc1 --region europe-west1
```

Esto creará un `job` (trabajo) en el cluster, ejecutado por Spark.

Verás el progreso en la propia consola, en algún sitio debería haber impreso el número de filas del trabajo cuando termine:

```terminal
Count: 1723
```

### Adjuntar archivos adicionales

En clase hemos trabajado haciendo uso de un archivo llamado `helpers.py`. Si se referencia el código de ese archivo desde cualquier script, es necesario adjuntarlo al trabajo mediante la opcion `--files`:

```sh
gcloud dataproc jobs submit pyspark prueba_dataproc.py --cluster dataproc1 --region europe-west1 --files=helpers.py
```

Los scripts pueden también residir en un bucket de Cloud Storage, simplemente reemplaza los normbres por la ruta completa de los archivos:

```terminal
gs://bigdataupv_code/prueba_dataproc.py
gs://bigdataupv_code/helpers.py
```

## Paso 5: Determinar el estado de los trabajos lanzados

Los trabajos ejecutados también son accesibles desde [la interfaz de usuario de Dataproc](https://console.cloud.google.com/dataproc/clusters/dataproc1/jobs), desde donde pueden consultarse los resultados.

Alternativamente se pueden listar todos los trabajos de una región, en nuestro caso `europe-west1`:

```sh
gcloud dataproc jobs list --region=europe-west1
```

Tras ejecutarlo debería mostrar una lista de trabajos:

```terminal
JOB_ID: 2c5c402a995e424ca24087498d559731
TYPE: pyspark
STATUS: DONE
```

### Consultar un determinado trabajo

Utilizando ese `JOB_ID` podemos también consultar el estado y los logs del trabajo, incluso antes de que finalize:

```sh
gcloud dataproc jobs wait 2c5c402a995e424ca24087498d559731 --project bigdataupv2021 --region europe-west1
```

## Paso 6: Eliminar el cluster

Para finalizar el ejercicio eliminaremos el cluster creado, de forma que se detendrá la facturación por uso de los recursos involucrados:

```sh
gcloud dataproc clusters delete dataproc1 --region=europe-west1
```

También es posible eliminarlo desde la consola de Google Cloud.

![](https://cloud.google.com/dataproc/images/dataproc-1-delete.png)

## Completado!

Recuerda eliminar el cluster de Dataproc al completar el ejercicio.

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

# Spark Docker Image

_WIP This documentation needs to be expanded_

## How to run Spark

By default, the image will run is pointing to `pyspark`, so running it without parameters will display directly the python repl:

```
docker run -ti luisbelloch/spark 
```

If you want to run one of the samples, simply mount a volume and run any of the python scripts:

```
docker run \
  -v $(greadlink -f ../../samples):/opt/samples \
  -w /opt/samples \
  -ti luisbelloch/spark spark-submit /opt/samples/compras_con_mas_de_un_descuento.py
```

All the executables from the Spark distribution are available in the container's path.

## Building the images

How to build the images:

```
docker build -t luisbelloch/spark .
docker tag luisbelloch/spark:2.10 luisbelloch/spark:latest
```

## Running Spark Master \ Workers

Variable `SPARK_NO_DAEMONIZE` is already set in the `Dockerfile`.

```
$ docker run -p 8080:8080 -d luisbelloch/spark start-master.sh
$ docker run -p 8081:8081 -d luisbelloch/spark start-slave.sh spark://localhost:7077
...
```

Note that workers connect to master node through 7077 exposed in localhost.

## Using Docker Compose

```
$ docker-compose up
```

Running `docker ps` will show containers and their ports mapped. Slaves can connect to master using internal DNS resolution, we've exposed the master node as `master`. Note that exposing worker nodes port is not straight-forward and we've leaved commented port mapping definition - we'll discuss that in class.

To scale up/down the cluster:

```
$ docker-compose scale worker=3
```

Beware desired state persist between runs.


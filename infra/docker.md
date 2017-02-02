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



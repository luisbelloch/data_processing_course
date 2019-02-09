# Setting up single-node Spark

This document describes how to download and setup Spark in your machine _without_ requiring a cluster setup.

> :warning: This is only intended for demo and learning purposes, please refer to the [official deployment guide](https://spark.apache.org/docs/latest/cluster-overview.html) for further information on how to properly deploy an Spark cluster.

In this repository you will find also other alternative options to run Spark locally:

  - [Spark on Docker](docker/docker.md)
  - [Spark on Kubernetes](kubernetes/kubernetes.md)
  - [Spark on Vagrant](vagrant.md)
  - [Spark on Google Cloud Dataproc](dataproc.md)
  - [PySpark Jupyter Notebook](pyspark-jupyter/README.md)

## Requirements

This setup assumes you have a linux machine with Java 8 and Python 3 installed. Assuming a Debian distribution, _stretch_ version, you can install required dependencies with the following commands:

```bash
sudo apt-get update
sudo apt-get install -y openjdk-8-jdk-headless python3-software-properties python3-numpy curl
```

## Downloading and unpacking Spark

We recommend to install Spark in `/opt/spark`. To download Spark package, you could use the following commands:

```bash
mkdir /opt/spark
curl http://apache.rediris.es/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz | tar -xz -C /opt/spark --strip-components=1
```

To make Spark binaries accessible add `/opt/spark/bin` to the `PATH`, by appending the following lines to your `.bashrc` file:

```bash
export PYSPARK_PYTHON=python3
export PATH=$PATH:/opt/spark/bin
```

After that, restart current shell to make sure `PATH` changes are applied.

## Testing the installation

Simply run the following command, you should get a value like `res0: Long = 100` in the console:

```bash
echo 'sc.parallelize(1 to 100).count()' | spark-shell
```

## Reducing log level

By default Spark is too verbose and it would output a ton of the information in the terminal. Optionally you could reduce the log level doing:

  1. Rename the file `/opt/spark/conf/log4j.properties.template` to `log4j.properties`, in the same directory.
  2. Edit the file and set `rootCategory` property to `ERROR` instead of `INFO`.

Use this two commands to do that automatically:

```bash
sed 's/rootCategory=INFO/rootCategory=ERROR/g' < /opt/spark/conf/log4j.properties.template > /opt/spark/conf/log4j.properties
```

## TL;DR Using helper script

All this procedure can be accomplished by a simple script included in the [classroom repository](https://github.com/luisbelloch/data_processing_course). Just clone the repository and run [`local_setup.sh`](../local_setup.sh):

```bash
git clone https://github.com/luisbelloch/data_processing_course.git
cd data_processing_course
./local_setup.sh
```

Spark will be installed in `data_processing_course/.spark`. Do not forget to add `bin` folder to the `$PATH`.

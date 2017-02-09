# Apache Beam Docker Image

## Basic usage

This folder contains a simple docker container to execute Apache Beam using python SDK, under direct runner. The image has been published in docker hub as [luisbelloch/beam:python2](https://hub.docker.com/r/luisbelloch/beam/):

```
$ docker pull luisbelloch/beam:python2
```

A simple word count sample can be run as:

```
$ docker run luisbelloch/beam:python2 python -m apache_beam.examples.wordcount \
    --input /etc/hosts --output /tmp/output.txt
```

We've included an script that will mount current folder as volume in `/data`:

```
$ ./beam -m apache_beam.examples.wordcount --input /etc/hosts --output /data/wordcount.txt
```

To run any script of the [samples](../../beam/) folder:

```
$ ./beam basic.py --input /data/compras_tiny.csv --output /data/purchases_summary.json
```

## Building the container

```
docker build -t luisbelloch/beam:python2 .
```


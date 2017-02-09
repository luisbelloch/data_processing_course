# Data Processing with Spark

Materials for the Advanced Data Processing course of the [Big Data Analytics](http://bigdata.inf.upv.es) Master at the Universitat Politècnica de València.

This course gives a 30 hours overview of many concepts, techniques and tools in data processing using Spark, including some key concepts from Apache Beam. We assume you're familiar with Python, but all the exercises can be easily followed in Java and Scala. We've included a Vagrant definition and docker images for both [Spark](infra/docker/docker.md) and [Beam](infra/beam/beam.md).

If you find a bug or you want to contribute some comments, please [fill an issue in this repository]() or simply [write us](mailto:bigdata@luisbelloch.es). You're free to reuse course materials, please follow details in the [license section](#license).

## Structure

### Part A - Spark

1. Brief intro to functional programming
2. Spark basics
3. PySpark: transformations, actions and basic IO
4. Spark SQL
5. MLib
6. Graphs
    - GraphX (Scala)
    - GraphFrames (Python)
7. Spark cluster deployment
    - Standalone cluster
    - [Docker](infra/docker/docker.md)
    - Kubernetes
8. Apache Beam
    - [Docker container using Python SDK](infra/beam/beam.md)
    - Slides (coming soon)
  

### Part B - Architecture Workshop

Team work using [Aronson's puzzle](https://en.wikipedia.org/wiki/Jigsaw_(teaching_technique)). We present a set of real case studies to solve and teams have to design and develop them using any technology available in the market today.  

In the first phase, the teams will split with the goal of becoming experts into a particular area and dig into the proposed tools and framework specifics. In the second phase, they'll return to their peers to design a system that covers use case requirement. There's a 15 minute presentation per team to share the results.

## Lecture Notes

To be added soon, stay tuned!

## Source Samples

- Functional programming (coming soon)
- Why you don't need big data tools
    - [poors_man_routes.sh](spark/data/poors_man_routes.sh) - bash superpowers
- Basic data processing using PySpark
    - [compras_con_mas_de_un_descuento.py](spark/compras_con_mas_de_un_descuento.py)
    - [compras_importe_total_agrupado_por_tx_id.py](spark/compras_importe_total_agrupado_por_tx_id.py)
    - [compras_conversion_a_dolares.py](spark/compras_conversion_a_dolares.py)
    - [compras_top_ten_countries.py](spark/compras_top_ten_countries.py)
    - [helpers.py](spark/helpers.py) - basic parse functions to get started quickly
- Spark SQL
    - [container.py](spark/container.py)
    - [container_convertir_a_parquet.py](spark/container_convertir_a_parquet.py)
    - [container_rdd_to_dataset.py](spark/container_rdd_to_dataset.py)
    - [container_databricks_csv.py](spark/container_databricks_csv.py)
    - [container_caching.py](spark/container_caching.py)
    - [container_partition.py](spark/container_partition.py)
- Spark Streaming
    - [hft.py](spark/stock_server.py) and [stock_server.rb](spark/stock_server.rb)
- MLib
    - [peliculas_0_ml.py](spark/peliculas_0_ml.py) - ALS intro
    - [peliculas_1_ml.py](spark/peliculas_1_ml.py) - Predictions
- GraphFrames
    - [friends.py](spark/friends.py) - Classic graph sample
    - [ship_routes.py](spark/ship_routes.py) - Shortest paths for ship routes
- Apache Beam
    - [basic.py](beam/basic.py)
    - [compras.py](beam/compras.py)
    - [compras_ptransform.py](beam/compras_ptransform.py)
    - [compras_ptransform_condensed.py](beam/compras_ptransform_condensed.py)
    - [compras_totales_por_pais.py](beam/compras_totales_por_pais.py)
- Deployment
    - [Standalone](local_setup.sh)
    - [Vagrant](Vagrantfile)
    - [Spark on Docker](infra/docker/docker.md)
    - [Beam on Docker](infra/beam/beam.md)
    - [Spark on Kubernetes]()

## Assignments

Final course assignments can be found in [this document](assignments/README.md). They are in Spanish, I'm planning to translate them for 2017 edition.

I'm not publishing the solutions to avoid remaking the exercises every year. There's a test suite using [py.test](http://pytest.org) to help you validate the results. If you're really interested on them, please write me to [bigdata@luisbelloch.es](mailto:bigdata@luisbelloch.es).

## Evaluation Criteria

> Self-sufficiency is the state of not requiring any aid, support, or interaction, for survival; it is therefore a type of personal or collective autonomy -  [Wikipedia](https://en.wikipedia.org/wiki/Self-sufficiency).

We follow a self-sufficiency principles for students to drive course goals. At the end of the course, students should have enough knowledge and tools to develop small data processing solutions their own. 

1. Student understands the underlying concepts behind Spark, and is able to write data processing scripts using PySpark, Spark SQL and MLib.
2. Student is capable of identify common data processing libraries and frameworks and their applications.
3. Student is capable to work in a team designing a system to cover a simple data processing scenario, understanding the basic implications of the choices they made on systems, languages, libraries and platforms.

## Readings and links

We recommend the following papers to expand knowledge on Spark and other data processing techniques:

- [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)
- [Discretized Streams: An Efficient and Fault-Tolerant Model for Stream Processing on Large Clusters](http://people.csail.mit.edu/matei/papers/2012/hotcloud_spark_streaming.pdf)
- [Spark SQL: Relational Data Processing in Spark](http://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf)
- [MLlib: Machine Learning in Apache Spark](http://www.jmlr.org/papers/volume17/15-237/15-237.pdf) 
- [GraphX: Unifying Data-Parallel and Graph-Parallel Analytics](https://amplab.cs.berkeley.edu/wp-content/uploads/2014/02/graphx.pdf)
- [Tachyon: Memory Throughput I/O for Cluster Computing Frameworks](http://people.eecs.berkeley.edu/~haoyuan/papers/2013_ladis_tachyon.pdf)
- [The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing](http://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf)
- [Apache Flink™: Stream and Batch Processing in a Single Engine](https://www.user.tu-berlin.de/asteriosk/assets/publications/flink-deb.pdf)
- [MillWheel: Fault-Tolerant Stream Processing at Internet Scale](http://research.google.com/pubs/pub41378.html)
- [Pig Latin: A Not-So-Foreign Language for Data Processing](http://infolab.stanford.edu/~olston/publications/sigmod08.pdf)
- [Interpreting the Data: Parallel Analysis with Sawzall](http://research.google.com/archive/sawzall.html)
- [Photon: Fault-tolerant and Scalable Joining of Continuous Data Streams](http://research.google.com/pubs/pub41318.html)

## Roadmap

Some ideas we might add in forthcoming course editions:

- Code samples in python notebooks
- ~~Apache Flink and Apache Beam~~ (2017)
- Add Tachyon content and exercises
- Add Kafka source to the streaming sample
- Introduce samples with Minio / InfiniSpan
- ~~Improve deployment scenarios and tools: Mesos, Chef, etc.~~ (2017)
- Monitoring using Prometheus and Grafana, provide ready-to-use docker containers
- Profiling of Spark applications (Scala only)
- Translate all content to English and Spanish

## License

Advanced Data Processing course materials.  
Copyright (C) 2016, Luis Belloch

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

### Recommended citation

> Luis Belloch, course materials for Advanced Data Processing, Spring 2016. Master on Big Data Analytics (http://bigdata.inf.upv.es), Universitat Politècnica de València. Downloaded on [DD Month YYYY].



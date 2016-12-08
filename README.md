# Data Processing with Spark 

Materials for the Advanced Data Processing course of the [Big Data Analytics](http://bigdata.inf.upv.es) Master at the Universitat Politècnica de València.

This course gives a 30 hours overview of many concepts, techniques and tools in data processing using Spark. We assume you're familiar with Python, but all the exercises can be easily followed in Java and Scala. We've included a Vagrant setup you can use to simplify your setup.

If you find a bug or you want to contribute some comments, please [fill an issue in this repository]() or simply [write us](mailto:bigdata@luisbelloch.es). You're free to reuse course materials, please follow details in the [license section](#license).

## Structure

### Part A - Spark

1. Brief intro to functional programming
2. Spark basics
3. PySpark: transformations, actions and basic IO
4. Spark SQL
5. MLib
6. GraphX (Scala only)
7. Spark cluster deployment

### Part B - Architecture Workshop

Team work using [Aronson's puzzle](https://en.wikipedia.org/wiki/Jigsaw_(teaching_technique)). We present a set of real case studies to solve and teams have to design and develop them using any technology available in the market today.  

In the first phase, the teams will split with the goal of becoming experts into a particular area and dig into the proposed tools and framework specifics. In the second phase, they'll return to their peers to design a system that covers use case requirement. There's a 15 minute presentation per team to share the results.

## Lecture Notes

To be added soon, stay tuned!

## Source Samples

- Basic data processing using PySpark  
    - [compras_con_mas_de_un_descuento.py](samples/compras_con_mas_de_un_descuento.py)
    - [compras_importe_total_agrupado_por_tx_id.py](samples/compras_importe_total_agrupado_por_tx_id.py)
    - [compras_conversion_a_dolares.py](samples/compras_conversion_a_dolares.py)
    - [compras_top_ten_countries.py](samples/compras_top_ten_countries.py)
    - [helpers.py](samples/helpers.py) - basic parse functions to get started quicly
- Spark SQL
    - [containers.py](samples/containers.py)
    - [container_convertir_a_parquet.py](samples/container_convertir_a_parquet.py)
- Spark Streaming
    - [hft.py](samples/stock_server.py) and [stock_server.rb](samples/stock_server.py)
- MLib
    - [peliculas_0_ml.py](samples/peliculas_0_ml.py) - ALS intro
    - [peliculas_1_ml.py](samples/peliculas_1_ml.py) - Predictions

## Assignments

Final course assignments can be found in [this document](assignments/README.md). They are in Spanish, I'm planning to translate them for 2017 edition.

I'm not publishing the solutions to avoid remaking the exercises every year. There's a test suite using [py.test](http://pytest.org) to help you validate the results. If you're really interested on them, please write me to [bigdata@luisbelloch.es](mailto:bigdata@luisbelloch.es).

## Evaluation Criteria

> Self-sufficiency is the state of not requiring any aid, support, or interaction, for survival; it is therefore a type of personal or collective autonomy -  [Wikipedia](https://en.wikipedia.org/wiki/Self-sufficiency).

We follow a self-sufficency principles for students to drive course goals. At the end of the course, students should have enough knowledge and tools to develop small data processing solutions their own. 

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
- Apache Flink and Apache Beam
- Add Tachyon content and exercises
- Add Kafka source to the streaming sample
- Improve deployment scenarios and tools: Mesos, Chef, etc.
- Monitoring using Prometheus and Grafana, provide ready-to-use docker containers
- Profiling of Spark applications (Scala only)

## License

Advanced Data Processing course materials.  
Copyright (C) 2016, Luis Belloch

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

### Recommended citation

> Luis Belloch, course materials for Advanced Data Processing, Spring 2016. Master on Big Data Analytics (http://bigdata.inf.upv.es), Universitat Politècnica de València. Downloaded on [DD Month YYYY].



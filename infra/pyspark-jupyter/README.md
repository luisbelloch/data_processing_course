# PySpark + Jupyter

This folder contains a docker container with PySpark ready to be run from a Jupyter Notebook.

To run it, simply do:

```
$ ./docker run -p 8888:8888 -ti luisbelloch/pyspark-jupyter
```

And navigate to [http://localhost:8888](http://localhost:8888). The password token will be displayed in the terminal.

There's a simple script that will also mount `data` folder used in samples. You can easily access to it from the notebook:

```
rdd = sc.textFile('./data/compras_tiny.csv')
rdd.take(2)
```


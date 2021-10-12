# PySpark + Jupyter

This folder contains a docker container with PySpark ready to be run from a Jupyter Notebook, specifically customized for the course.

For more general uses, we recommend to use the official [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html). This image itself is derived from `jupyter/pyspark-notebook` one.

To run it, simply do:

```bash
docker run -p 8888:8888 -ti luisbelloch/pyspark-jupyter
```

And navigate to [http://localhost:8888](http://localhost:8888). The password token will be displayed in the terminal.

This image contains `data` folder used in the examples. You can easily access to it from the notebook:

```python
rdd = sc.textFile('./data/compras_tiny.csv')
rdd.take(2)
```


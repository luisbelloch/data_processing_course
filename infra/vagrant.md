# Using PySpark inside a Vagrant machine

We have created a Vagrant setup using Ansible that will download and unpack Spark inside the generated machine.

> :warning: This is only intended for demo and learning purposes, please refer to the [official deployment guide](https://spark.apache.org/docs/latest/cluster-overview.html) for further information on how to properly deploy an Spark cluster.

To bootstrap the machine, do:

```bash
git clone https://github.com/luisbelloch/data_processing_course.git
cd data_processing_course
vagrant up
```

Once the process completes you can access the machine by using:

```bash
vagrant ssh
```

Remember that you can access the _host_ machine files using the `/vagrant` folder from the inside of the VM.

## Testing the installation

Simply run the following command, you should get a value like `res0: Long = 100` in the console:

```bash
echo 'sc.parallelize(1 to 100).count()' | spark-shell
```

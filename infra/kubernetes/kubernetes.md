# Spark-on-Kubernetes

Code is based on [official Kubernetes examples](https://github.com/kubernetes/kubernetes/tree/master/examples/spark) and the [Spark 2.1 docker image](../docker/docker.md) used during the course.

## Prerequisites

We recommend to work locally using `minikube`. Install [kubectl](https://kubernetes.io/docs/user-guide/prereqs/) and [minikube](https://kubernetes.io/docs/getting-started-guides/minikube/) from the official sources.

After installing `minikube` we will push our Spark docker image to the internal Kubernetes registry. Use `minikube docker-env` to point current docker client to our cluster.

```
$ eval $(minikube docker-env)
$ docker build -t luisbelloch/spark ../infra/docker
$ docker push luisbelloch/spark
```

Alternatively you could use GRC images, just point the image containers to `gcr.io/google_containers/spark:1.5.2_v1`.

## Cluster provisioning

First of all, we'll create a new namespace for our cluster and configure a context for `kubectl`. From this point, all the `kubectl` commands will be confined to that namespace.

```
$ kubectl create -f namespace.yaml
$ kubectl config set-context spark --namespace=bigdataupv-spark --user=minikube --cluster=minikube
$ kubectl config use-context spark
```

### Master node

First thing we'll deploy is the Spark Master. We've defined a replication controller that will create just one container to host it. Note that if the master goes down, Kubernetes will automatically respawn the container.

```
$ kubectl create -f master-controller.yaml
$ kubectl get pods
NAME                            READY     STATUS              RESTARTS   AGE
spark-master-controller-5pzdb   0/1       ContainerCreating   0          1s
```

If you want to submit again the configuration after some changes, use command `apply` and Kubernetes will reconfigure the controller again. Although you can use the UI for this, notice best practice is to reapply configurations.

```
$ kubectl apply -f master-controller.yaml
```

Now we can check pod is up and running and master has elected as leader

```
$ kubectl get pods
NAME                            READY     STATUS    RESTARTS   AGE
spark-master-controller-78dqq   1/1       Running   0          2m

$ kubectl logs spark-master-controller-78dqq
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
17/02/09 20:42:57 INFO Master: Started daemon with process name: 12@spark-master-controller-78dqq
...
17/02/09 20:42:58 INFO Master: I have been elected leader! New state: ALIVE
```

Note that the replication controller has `replicas: 1`, only one pod will be created to act as the master. The master node should declare two services: one in port 7077 to communicate with workers, and another in port 8080 serving the web UI:

```
$ kubectl apply -f master-service.yaml
```

Spark UI can be accessed starting `kubectl proxy` and accessing directly to this URL:

```
http://127.0.0.1:8001/api/v1/proxy/namespaces/bigdataupv-spark/pods/spark-master-controller-78dqq:8080/
```

### Slaves

Starting slaves is pretty straightforward. Remember we've exposed the master node under the name `spark-master`, and therefore it will be accessible from other pods using simple DNS calls. The following command will create a replication controller for the slaves, starting with one pod:

```
$ kubectl apply -f slave-controller.yaml

$ kubectl get rc -o wide
NAME                      DESIRED   CURRENT   READY     AGE       CONTAINER(S)   IMAGE(S)            SELECTOR
spark-master-controller   1         1         1         36m       spark-master   luisbelloch/spark   component=spark-master
spark-worker-controller   1         1         1         3m        spark-worker   luisbelloch/spark   component=spark-worker
```

### Accessing to PySpark

We can open a `PySpark` session directly in the master node, using `exec` command:

```
$ kubectl exec spark-master-controller-78dqq -ti -- pyspark --master=spark://spark-master-controller-78dqq:7077
```

If you ever need an interactive login, simply replace `pyspark` by `/bin/bash`.

### Scaling the cluster

```
$ kubectl scale --replicas=4 rc/spark-worker-controller
replicationcontroller "spark-worker-controller" scaled

$ kubectl get pods
NAME                            READY     STATUS              RESTARTS   AGE
spark-master-controller-78dqq   1/1       Running             0          40m
spark-worker-controller-9r9vd   1/1       Running             0          8s
spark-worker-controller-sp3tt   1/1       Running             0          1m
spark-worker-controller-srvdm   0/1       ContainerCreating   0          8s
```

## Problems not addressed

As we've seen in class, this has been an exercise to play with Spark deployment options and much deeper thoughts are needed before going to production. Generally speaking, Spark needs a bit more of work to make it aware of the environment it executes, particularly the UIs. In the Kubernetes repository there are few issues that you may follow up close to get more information:

- [#16517](kubernetes/kubernetes#16517) Has a good compendium of problems and things that doesn't work out of the box.
- [#34377](kubernetes/kubernetes#34377) Describes some ideas to support other Spark deployment modes than the "standalone" one.
- [#16949](kubernetes/kubernetes#16949) Talks about the problem with slave UIs ports and how it may be resolved.

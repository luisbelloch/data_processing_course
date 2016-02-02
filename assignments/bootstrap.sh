#!/usr/bin/env bash

apt-get update
apt-get install -y software-properties-common python-software-properties curl

# Java 8
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
add-apt-repository -y ppa:webupd8team/java  
apt-get update 
apt-get install -y oracle-java8-installer 

# Spark
SPARK_PKG=spark-1.6.0-bin-hadoop2.6
SPARK_HOME=/opt/spark

wget http://d3kbcqa49mib13.cloudfront.net/${SPARK_PKG}.tgz
tar xvfz ${SPARK_PKG}.tgz
mv $SPARK_PKG /opt/
ln -s /opt/$SPARK_PKG $SPARK_HOME

mv $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties
sed -i s/rootCategory=INFO/rootCategory=ERROR/ $SPARK_HOME/conf/log4j.properties

echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle/' >> /home/vagrant/.bashrc
echo "export SPARK_HOME=$SPARK_HOME" >> /home/vagrant/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin" >> /home/vagrant/.bashrc

# Py.test
apt-get install -y python-pip
pip install pytest


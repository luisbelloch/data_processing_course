#!/usr/bin/env bash

apt-get update
apt-get install -y software-properties-common python-software-properties curl git

# Java 8
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
add-apt-repository -y ppa:webupd8team/java  
apt-get update 
apt-get install -y oracle-java8-installer 

LHOME=/home/ubuntu

# Spark
export SPARK_HOME=/opt/spark
$LHOME/spark_setup.sh

git clone https://github.com/luisbelloch/data_processing_course.git $LHOME/data_processing_course

echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle/' >> $LHOME/.bashrc
echo "export PATH=$SPARK_HOME/bin:$PATH" >> $LHOME/.bashrc



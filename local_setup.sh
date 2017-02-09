#!/bin/bash
set -eoi pipefail
SPARK_PKG=${SPARK_PKG:-spark-2.1.0-bin-hadoop2.7}
SPARK_HOME=${SPARK_HOME:-$(pwd)/.spark}

if [ -t 1 ]; then
    readonly colors=$(tput colors)
    if [ -n "$colors" ]; then
        readonly c_step="$(tput setaf 6)"
        readonly c_error="$(tput setaf 1)"
        readonly c_norm="$(tput sgr0)"
    fi
fi

if [ -d "${SPARK_HOME}" ]; then
    echo "${c_error}ERROR${c_norm}: Folder already exists '$SPARK_HOME'"
    echo "Set SPARK_HOME to an empty folder before running this script or make sure there's no 'spark' folder in current directory."
    exit -1
fi

echo "${c_step}[0] Destination: ${SPARK_HOME}${c_norm}"
echo "${c_step}[1] Downloading and unpacking $SPARK_PKG.tgz${c_norm}"
mkdir -p "${SPARK_HOME}"
curl -s http://d3kbcqa49mib13.cloudfront.net/${SPARK_PKG}.tgz | tar -xz -C "${SPARK_HOME}" --strip-components=1

echo "${c_step}[2] Reducing log level${c_norm}"
cp "${SPARK_HOME}"/conf/log4j.properties.template "${SPARK_HOME}"/conf/log4j.properties
sed -ibak 's/rootCategory=INFO/rootCategory=ERROR/g' "${SPARK_HOME}"/conf/log4j.properties

echo -e "${c_step}[3] Testing setup${c_norm}"
echo 'sc.parallelize(1 to 100).count()' | "${SPARK_HOME}"/bin/spark-shell
rm -rf derby.log metastore_db

echo
echo "${c_step}DONE! Local setup completed${c_norm}"
echo "Spark unpacked properly. You can now modify your path:"
echo "export PATH=${SPARK_HOME// /\\ /}:\$PATH"


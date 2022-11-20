#!/bin/bash
set -euo pipefail
SPARK_URL=${SPARK_URL:-https://downloads.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz}
SPARK_PKG=${SPARK_URL##*/}
SPARK_HOME=${SPARK_HOME:-$(pwd)/.spark}

if [ -t 1 ]; then
    readonly colors=$(tput colors)
    if [ -n "$colors" ]; then
        readonly c_step="$(tput setaf 6)"
        readonly c_error="$(tput setaf 1)"
        readonly c_norm="$(tput sgr0)"
    fi
fi

stderr() { >&2 echo "$@"; }

if [[ -d "${SPARK_HOME}" ]]; then
    stderr "${c_error}ERROR${c_norm}: Folder already exists '$SPARK_HOME'"
    stderr "Set SPARK_HOME to an empty folder before running this script or make sure there's no 'spark' folder in current directory."
    exit 1
fi

stderr "${c_step}[0] Destination: ${SPARK_HOME}${c_norm}"
stderr "${c_step}[1] Downloading and unpacking $SPARK_PKG.tgz${c_norm}"
mkdir -p "${SPARK_HOME}"
curl -s "${SPARK_URL}" | tar -xz -C "${SPARK_HOME}" --strip-components=1

stderr "${c_step}[2] Reducing log level${c_norm}"
cp "${SPARK_HOME}"/conf/log4j2.properties.template "${SPARK_HOME}"/conf/log4j2.properties
sed -ibak 's/rootLogger.level = info/rootLogger.level = error/g' "${SPARK_HOME}/conf/log4j2.properties"

stderr "${c_step}[3] Testing setup${c_norm}"
echo 'sc.parallelize(1 to 100).count()' | "${SPARK_HOME}"/bin/spark-shell
rm -rf derby.log metastore_db

stderr
stderr "${c_step}DONE! Local setup completed${c_norm}"
stderr "Spark unpacked properly. You can now modify your path:"
echo "export PATH=${SPARK_HOME// /\\ /}/bin:\$PATH"


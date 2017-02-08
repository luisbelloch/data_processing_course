#!/bin/bash
set -eoi pipefail

readonly PKG="graphframes:graphframes:0.3.0-spark2.0-s_2.11"
command=spark-submit
if [ $# -eq 0 ]; then
    command=pyspark
fi

$command --packages $PKG "$*"
exit $?


#!/bin/bash
set -euo pipefail

readonly PKG="graphframes:graphframes:0.8.1-spark3.0-s_2.12"
if [ $# -eq 0 ]; then
    pyspark --packages $PKG
else
    spark-submit --packages $PKG "$*"
fi

exit $?


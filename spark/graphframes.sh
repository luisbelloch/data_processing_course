#!/bin/bash
set -euo pipefail

# 0.5.0 seems to be broken at this point,
# check this issue https://git.io/vNjRt
readonly PKG="graphframes:graphframes:0.4.0-spark2.1-s_2.11"
if [ $# -eq 0 ]; then
    pyspark --packages $PKG
else
    spark-submit --packages $PKG "$*"
fi

exit $?


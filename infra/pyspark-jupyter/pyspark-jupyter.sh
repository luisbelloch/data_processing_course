#!/bin/bash
set -eou pipefail

abs_path() {
    echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

docker run -p 8888:8888 \
    -v $(abs_path "../../data"):/opt/notebook/data \
    -v $(abs_path "../../spark"):/opt/notebook/spark \
    -ti luisbelloch/pyspark-jupyter


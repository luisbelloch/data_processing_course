#!/bin/bash
set -eou pipefail

readonly IP=$(awk 'END{print $1}' /etc/hosts)
export PYSPARK_DRIVER_PYTHON_OPTS="notebook --ip \"${IP}\" --allow-root --port 8888"
pyspark


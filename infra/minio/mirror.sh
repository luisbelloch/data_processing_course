#!/bin/bash
set -eou pipefail
readonly BUCKET=local/data
./mc mb -p "${BUCKET}"
./mc mirror --remove data "${BUCKET}"


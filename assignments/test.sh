#!/bin/bash
readonly WORKDIR=/opt/tests/assignments
docker run -v $(pwd):${WORKDIR} -w ${WORKDIR} -ti luisbelloch/spark-assignments pytest -v


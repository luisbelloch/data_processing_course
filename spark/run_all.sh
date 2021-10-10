#!/bin/bash

readonly c_step="$(tput setaf 6)"
readonly c_norm="$(tput sgr0)"
readonly excluded=(helpers.py hft.py container_caching.py)

for file in *.py; do
  if [[ ! " ${excluded[*]} " =~ " ${file} " ]]; then
    echo -e "${c_step}Running${c_norm} $file"
    spark-submit $file 2>/dev/null
  fi
done

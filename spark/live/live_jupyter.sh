#!/bin/bash
set -eou pipefail

fswatch ../live.ipynb | while read -r fpath; do \
  echo -e "\033[0;36mRELOAD\033[0m $fpath $(date +"%H%m%S")"
  jupyter nbconvert ../live.ipynb --to html --output-dir="$(pwd)"
  gsutil -h "Cache-Control:no-cache,max-age=0" \
    cp live.html gs://bigdata.luisbelloch.es/en_directo.html
  # scp live/live.html root@live.luisbelloch.es:/var/www/html/index.html
done


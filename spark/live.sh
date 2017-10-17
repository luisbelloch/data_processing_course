#!/bin/bash
set -euo pipefail

fswatch live.py | while read -r fpath; do \
    echo -e "\033[0;36mRELOAD\033[0m $fpath $(date +"%H%m%S")"
    pygmentize -f html -O full,linenos=1 -o live.html live.py
    scp live.html root@live.luisbelloch.es:/var/www/html/index.html
done


#!/bin/bash
set -euo pipefail

fswatch live.py | while read -r fpath; do \
    clear
    echo -e "\033[0;36mRELOAD\033[0m $fpath $(date +"%H%M%S")"
    spark-submit live.py
done


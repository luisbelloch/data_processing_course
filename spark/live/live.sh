#!/bin/bash
set -euo pipefail

fswatch ../live.py | while read -r fpath; do \
    echo -e "\033[0;36mRELOAD\033[0m $fpath $(date +"%H%M%S")"
    echo -e "# $(date +"%H:%M:%S")\n" | cat - ../live.py > live_mod.py
    sed -e '/-python">/r./live_mod.py' live_template.html > live.html
    ./gsutil -h "Cache-Control:no-cache,max-age=0" \
        cp /tmp/current/live.html gs://bigdata.luisbelloch.es/en_directo.html

    # echo -e "# $(date +"%H:%M:%S")\n" | cat - live.py | pygmentize -f html -O full,linenos=1 -o live.html
    # scp live.html root@live.luisbelloch.es:/var/www/html/index.html
done


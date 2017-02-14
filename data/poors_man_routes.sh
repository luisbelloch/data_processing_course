#!/bin/bash
set -euo pipefail

# Poor's man big data - bash edition

function clean_up {
    rm -rf random_ships*
}
trap clean_up EXIT

# Read ship_imo and ship_name
mkfifo random_ships
cut -d ";" -f1,2 containers_tiny.csv | uniq | tail -n +2 | sed "s/;/|/g" > random_ships &

# Place random numbers
while read f; do 
    shuf country_codes.csv | head -n $(((RANDOM % 10) + 1)) | \
       sed "s/,/|/g" | awk '{ printf "%d|'"$f"'|%s\n", i++, $0 }'
done < random_ships


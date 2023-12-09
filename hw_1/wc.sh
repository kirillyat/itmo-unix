#!/bin/bash

totallines=0
totalwords=0
totalbytes=0

for file in "$@"
do
    if [ -f "$file" ]; then
        lines=$(wc -l < "$file")
        words=$(wc -w < "$file")
        bytes=$(wc -c < "$file")

        totallines=$((totallines + lines))
        totalwords=$((totalwords + words))
        totalbytes=$((totalbytes + bytes))

        echo "$lines $words $bytes $file"
    fi
done

if [ $# -gt 1 ]; then
    echo "$totallines $totalwords $totalbytes total"
fi

if  $# -eq 0 ; then
    lines=$(wc -l)
    words=$(wc -w)
    bytes=$(wc -c)

    echo "$lines $words $bytes"
fi
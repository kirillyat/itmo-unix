#!/bin/bash

if [ "$#" -lt 1 ]; then
    tail -n 17
fi

for file in "$@"; do
    if [ "$#" -gt 1 ]; then
        
        echo "==> $file <=="
        
    fi
    tail -n 10 "$file"
    echo    
done

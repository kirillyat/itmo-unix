#!/bin/bash

input_file=$1

if [[ -z "$input_file" ]]; then
    cat -n
else
    cat -n $input_file
fi
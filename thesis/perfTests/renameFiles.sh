#!/bin/bash


if ! [  $1 ]; then
    echo "Zadat slozku"
fi

i=1
for file in $1*.csv*; do
    mv $file ${file%.csv*}-$i.csv
    
    i=`expr $i + 1`
done



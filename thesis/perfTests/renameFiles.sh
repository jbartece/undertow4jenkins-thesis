#!/bin/bash


if ! [  $1 ]; then
    echo "Enter directory name"
    exit 1
fi

i=0
for file in $1*.csv*; do
    targetName=`echo ${file%.csv*} | sed 's/[0-9]//g'`
    
    mv $file "$targetName$i.csv"
    
    i=`expr $i + 1`
done



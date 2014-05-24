#!/bin/bash

resultsDir="results"
undertowDir="undertow"
origDir="orig"

heading="stableTime;stableResponseTimeArithmeticAverage;stableResponseTimeStandardDeviation"

for dir in $resultsDir/*; do
    if ! [ -d $dir ];then
        continue
    fi
    
    targetFileName="$resultsDir/`echo "$dir" | sed -r 's/[/]/_/g'`.csv"
    echo $heading > $targetFileName

    
    echo "#original;;" >> $targetFileName
    for file in $dir/$origDir/*; do
        if [ "$resultsDir/getFreestyleJob" == "$dir" ]; then
            ./countStatistics.py "true" < $file >> $targetFileName
        else
            ./countStatistics.py  < $file >> $targetFileName
        fi
    done


    echo "#undertow4jenkins;;" >> $targetFileName
    for file in $dir/$undertowDir/*; do
        if [ "$resultsDir/getFreestyleJob" == "$dir" ]; then
            ./countStatistics.py "true" < $file >> $targetFileName
        else
            ./countStatistics.py  < $file >> $targetFileName
        fi
    done


done



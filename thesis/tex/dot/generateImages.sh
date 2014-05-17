#!/bin/bash

for dotImg in *.dot; do
    dot -Tpng $dotImg > `echo $dotImg | sed s/\.dot/\.png/`
done
    


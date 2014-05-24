#!/usr/bin/python3
import sys
import re
import math

def checkDifference(prev, act):
    if prev == -1:
        return False
        

    diff = math.fabs(prev - act)
    relDiff = diff / prev
    if relDiff < 0.001 and diff < 1 and act < 3000:
        return True
    else:
        return False

if __name__ == "__main__":
    pattern = re.compile(r"(.+);.+;(.+);.*")
    i = 0
    prev = -1.0

    for line in sys.stdin:
        if i == 0:
            i += 1
            continue

        matcher = pattern.match(line)

        if matcher:
            timePast =matcher.group(1)
            timeStr = matcher.group(2)
            if timeStr == "null":
                continue
            time = float(timeStr)

            if checkDifference(prev, time):
                print("Ustaleno. Cas: ", timePast)
                break

            prev = time    
            #print("Time: ", time)
        else:
            print("Match failed for line ", line)


        i += 1


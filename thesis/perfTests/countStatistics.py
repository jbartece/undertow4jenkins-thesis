#!/usr/bin/python3
import sys
import re
import math


class StatisticWorker:
    checkMaxResponseTime = False
    listLen = 3
    
    def __init__(self, checkMaxResponseTime):
        self.checkMaxResponseTime = checkMaxResponseTime
        
    def checkDifference(self, l, act):
        if len(l)  != self.listLen:
            return False
            
        for prevTime in l:
            if not self.checkSingleDiff(prevTime, act):
                return False

        return True
            
    def checkSingleDiff(self, prev, act):        
        diff = math.fabs(prev - act)
        relDiff = diff / act
        if self.compareDiff(relDiff, act):
            return True
        else:
            return False

    def compareDiff(self, relDiff, act):
        if self.checkMaxResponseTime:
            if relDiff < 0.005 and act < 4000:
                return True
            else:
                return False
        else:
            if relDiff < 0.005:
                return True
            else:
                return False

    def addItem(self, l, time):
        if len(l) < self.listLen:
            return l + [time]
        else:
            return l[1:] + [time]

    def run(self):
        pattern = re.compile(r"(.+);.+;(.+);.*")
        firstIter = True
        stable = False
        actList = []
        stableValuesList = []

        for line in sys.stdin:
            if firstIter:
                firstIter = False
                continue

            matcher = pattern.match(line)

            if matcher:
                timePast = matcher.group(1)
                timeStr = matcher.group(2)
                if timeStr == "null":
                    continue
                time = float(timeStr)

                if stable:
                    stableValuesList.append(time)

                else:    
                    if self.checkDifference(actList, time):
                        stable = True
                        stableTime = timePast
                        #print("Stable time: ", timePast)

                    actList = self.addItem(actList, time)

            else:
                print("Match failed! Line ", line)

        arithAvg = self.countArithAverage(stableValuesList)
        stdDeviation = self.countStdDeviation(stableValuesList, arithAvg)

        self.reportResults(stableTime, arithAvg, stdDeviation)

        #print("Response time average: ", arithAvg)

    def countStdDeviation(self, stableValuesList, arithAvg):
        
        sum = 0
        for singleValue in stableValuesList:
            sum += (singleValue - arithAvg)**2

        return math.sqrt(sum /len(stableValuesList)) 

    def countArithAverage(self, l):
        length = len(l)
        if length == 0:
            return "No values"
            
        sum = 0
        for singleValue in l:
            sum += singleValue

        return sum / len(l)

    def reportResults(self, stableTime, arithAvg, stdDeviation):
        print(stableTime, ";", arithAvg, ";", stdDeviation, sep="")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = True
    else:
        flag = False
    
    worker = StatisticWorker(flag)
    worker.run()

    


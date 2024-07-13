import sys

currentH, currentM, currentS = map(int, sys.stdin.readline().strip().split(':'))
startH, startM, startS = map(int, sys.stdin.readline().strip().split(':'))

currentTime = currentH * 60 * 60 + currentM * 60 + currentS
startTime = startH * 60 * 60 + startM * 60 + startS

leftTime = (startTime - currentTime)  if currentTime < startTime else 60*60*24 - abs(startTime - currentTime)

leftH = leftTime // (60 * 60)
leftTime = leftTime % (60 * 60)
leftM = leftTime // 60
leftTime = leftTime % 60
leftS = leftTime

print('%02d:%02d:%02d'%(leftH, leftM, leftS))
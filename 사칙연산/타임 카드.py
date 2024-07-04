import sys

for i in range(3):
  startH, startM, startS, finishH, finishM, finishS = map(int, sys.stdin.readline().strip().split())

  startTime = startH * 60 * 60 + startM * 60 + startS
  finishTime = finishH * 60 * 60 + finishM * 60 + finishS

  totalTime = finishTime - startTime

  totalTimeH = totalTime // (60*60)
  totalTime -= totalTimeH * 60 * 60
  totalTimeM  = totalTime // 60
  totalTimeS = totalTime % 60

  print(totalTimeH, totalTimeM, totalTimeS)

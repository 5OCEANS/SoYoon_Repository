import sys, math

T = int(sys.stdin.readline())
aList = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
bList = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
cList = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
type = ['T', 'F', 'F', 'T', 'F', 'F', 'T']
for i in range(T):
  scoreList = list(map(int, sys.stdin.readline().strip().split()))
  totalScore = 0
  for i in range(len(scoreList)):
    if type[i] == 'T':
      score = math.floor(aList[i] * (pow((bList[i]-scoreList[i]), cList[i])))
      totalScore += score
    else:
      score = math.floor(aList[i] * (pow((scoreList[i]-bList[i]), cList[i])))
      totalScore += score
  print(totalScore)
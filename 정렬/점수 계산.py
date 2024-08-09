import sys

scoreDict = {}

for i in range(1, 9):
  score = int(sys.stdin.readline())
  scoreDict[score] = str(i)

sortedScoreDict = dict(sorted(scoreDict.items(), key=lambda x: (-x[0])))

scoreList = list(sortedScoreDict.keys())[:5]
orderList = sorted(list(sortedScoreDict.values())[:5])

print(sum(scoreList))
print(' '.join(orderList))
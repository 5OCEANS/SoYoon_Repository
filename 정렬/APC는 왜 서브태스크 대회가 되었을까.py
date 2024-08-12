import sys

N, L, K = map(int, sys.stdin.readline().strip().split())
scoreList = []

for i in range(N):
  sub1, sub2 = map(int, sys.stdin.readline().strip().split())
  if sub2 <= L:
    scoreList.append(140)
  elif sub1 <= L:
    scoreList.append(100)

sortedScoreList = sorted(scoreList, reverse=True)
totalScore = sum(sortedScoreList[:K])

print(totalScore)
import sys

N = int(sys.stdin.readline())
scoreList = []

for i in range(N):
  student = list(map(int, sys.stdin.readline().strip().split()))
  scoreList.append(student)

sortedScoreList = sorted(scoreList, key= lambda x:(x[2]), reverse=True)

print(sortedScoreList[0][0], sortedScoreList[0][1])
print(sortedScoreList[1][0], sortedScoreList[1][1])

if sortedScoreList[0][0] == sortedScoreList[1][0] == sortedScoreList[2][0]:
  index = 2
  while sortedScoreList[index][0] == sortedScoreList[0][0]:
    index += 1
  print(sortedScoreList[index][0], sortedScoreList[index][1])
else:
  print(sortedScoreList[2][0], sortedScoreList[2][1])
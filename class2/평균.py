subjectCnt = int(input())

scoreList = list(map(int, input().split()))
avgnewScore = 0

for i in range(0, subjectCnt):
  newScore = scoreList[i] / max(scoreList) * 100
  avgnewScore += newScore

print(avgnewScore/subjectCnt)
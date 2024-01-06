caseCnt = int(input())
totalScore = 0

for i in range(0, caseCnt):
  oxList = list(input())
  score = 1
  for i in oxList:
    if i == 'O':
      totalScore += score
      score += 1
    if i == 'X':
      totalScore += 0
      score = 1
  print(totalScore)
  totalScore = 0
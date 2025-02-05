import sys

scoreList = list(sys.stdin.readline().strip())
aScore = 0
bScore = 0
for i in range(len(scoreList)//2):
  if scoreList[i*2] == 'A':
    aScore += int(scoreList[i*2+1])
  else:
    bScore += int(scoreList[i*2+1])
  if aScore >= 11 and (aScore - 2) >= bScore:
    print('A')
    break
  elif bScore >= 11 and (bScore - 2) >= aScore:
    print('B')
    break
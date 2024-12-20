import sys, math

def check_score(x, y):
  distance = math.sqrt(x**2 + y**2)
  if distance <= 3:
    return 100
  elif distance <= 6:
    return 80
  elif distance <= 9:
    return 60
  elif distance <= 12:
    return 40
  elif distance <= 15:
    return 20
  else:
    return 0

T = int(sys.stdin.readline())
for _ in range(T):
  scoreList = list(map(float, sys.stdin.readline().strip().split()))
  firstPlayerScore = 0
  secondPlayerScore = 0
  for i in range(0, 5, 2):
    firstPlayerScore += check_score(scoreList[i], scoreList[i+1])
  for i in range(6, 11, 2):
    secondPlayerScore += check_score(scoreList[i], scoreList[i+1])
  print('SCORE: '+str(firstPlayerScore)+' to '+str(secondPlayerScore)+',', end=' ')
  if firstPlayerScore == secondPlayerScore:
    print('TIE.')
  elif firstPlayerScore > secondPlayerScore:
    print('PLAYER 1 WINS.')
  else:
    print('PLAYER 2 WINS.')
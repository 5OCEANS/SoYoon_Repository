import sys

T = int(sys.stdin.readline())

for _ in range(T):
  totalyScore = 0
  totalkScore = 0
  for _ in range(9):
    y, k = map(int, sys.stdin.readline().strip().split())
    totalyScore += y
    totalkScore += k
  if totalyScore > totalkScore:
    print('Yonsei')
  elif totalyScore == totalkScore:
    print('Draw')
  else:
    print('Korea')
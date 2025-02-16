import sys

T = int(sys.stdin.readline())
for i in range(T):
  chocoX, chocoY, ruleX, ruleY = map(int, sys.stdin.readline().strip().split())
  chocoMap = [[False]*chocoX for _ in range(chocoY)]

  count = 0
  isKnight = True

  while chocoX >= 0 and chocoY >= 0:
    for k in range(chocoY):
      for j in range(chocoX):
        chocoMap[k][j] = isKnight
    chocoX -= ruleX
    chocoY -= ruleY
    isKnight = not isKnight
  
  for k in range(len(chocoMap)):
    for j in range(len(chocoMap[0])):
      if chocoMap[k][j]:
        count += 1
  print(count)
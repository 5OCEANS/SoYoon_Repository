import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  N = int(sys.stdin.readline().strip())
  chrList = list(sys.stdin.readline().strip().split())

  newString = chrList[0]

  for j in range(1, N):
    if ord(newString[0]) < ord(chrList[j]):
      newString += chrList[j]
    else:
      newString = chrList[j] + newString
  
  print(newString)
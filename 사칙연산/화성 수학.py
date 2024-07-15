import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  numList = list(sys.stdin.readline().strip().split())
  ans = float(numList[0])

  for j in range(1, len(numList)):
    if numList[j] == '@':
      ans *= 3
    elif numList[j] == '%':
      ans += 5
    elif numList[j] == '#':
      ans -= 7
  
  print('%0.2f' %(ans))
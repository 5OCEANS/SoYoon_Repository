import sys, math

T = int(sys.stdin.readline())

for i in range(T):
  string = sys.stdin.readline().strip()
  
  n = int(math.sqrt(len(string)))
  stringList = []

  for i in range(n):
    stringList.append(list(string[i*n:i*n+n]))
  
  stringList = list(zip(*stringList))

  for i in range(n):
    print(''.join(stringList[n-1-i]), end = '')

  print()
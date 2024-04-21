import sys

N = int(sys.stdin.readline())

for i in range(N):
  stringList = sys.stdin.readline().strip().split()
  stringList = stringList[::-1]

  print('Case #%d: ' %(i+1), end = '')

  for j in stringList:
    print(j, end = ' ')    
  
  print()
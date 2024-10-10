import sys

M = int(sys.stdin.readline().strip())
cardict = dict()

for i in range(M):
  time, num = map(int, sys.stdin.readline().strip().split())
  
  if num in cardict:
    print(num, time - cardict[num])
  else:
    cardict[num] = time
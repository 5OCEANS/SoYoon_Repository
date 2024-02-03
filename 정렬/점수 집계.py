import sys

T = int(sys.stdin.readline())

for i in range(T):
  numlist = list(map(int, sys.stdin.readline().strip().split()))
  numlist.sort()
  
  if numlist[3] - numlist[1] >= 4:
    print('KIN')
  else:
    print(sum(numlist[1:4]))
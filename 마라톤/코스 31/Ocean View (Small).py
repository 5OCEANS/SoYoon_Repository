import sys

T = int(sys.stdin.readline())
for case in range(T):
  N = int(sys.stdin.readline())
  houseList = list(map(int, sys.stdin.readline().strip().split()))
  count = 0
  front = houseList[0]
  for i in range(1, N):
    if front >= houseList[i]:
      count += 1
    front = houseList[i]
  print('Case #%d: %d' %(case+1, count))
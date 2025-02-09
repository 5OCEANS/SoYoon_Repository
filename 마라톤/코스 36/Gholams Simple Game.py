import sys

T = int(sys.stdin.readline())
for _ in range(T):
  m, n = map(int, sys.stdin.readline().strip().split())
  tileList = list(map(int, sys.stdin.readline().strip().split()))
  startIndex = -1
  ans = 0
  if 3 in tileList: # 왼쪽으로 이동
    startIndex = tileList.index(3)
    move = -1   
  else: # 오른쪽으로 이동
    startIndex = tileList.index(2)
    move = 1
  for i in range(n):
    if ((startIndex + move) <= -1) or ((startIndex + move) >= len(tileList)):
      move *= -1
    startIndex += move
    if tileList[startIndex] == 0:
      ans += 1
  print(ans) 
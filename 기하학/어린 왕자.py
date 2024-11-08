import sys, math

T = int(sys.stdin.readline())

for i in range(T):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
  count = 0
  n = int(sys.stdin.readline())
  for j in range(n):
    cx, cy, r = map(int, sys.stdin.readline().strip().split())

    distance1toc = math.sqrt((x1-cx)**2 + (y1-cy)**2)
    distance2toc = math.sqrt((x2-cx)**2 + (y2-cy)**2)

    distanceList = sorted([distance1toc, distance2toc])

    if distanceList[0] < r and distanceList[1] < r: # 출발점과 도착점이 모두 행성 내부에 있어 진입/이탈이 필요없는 경우
      continue
    elif distanceList[0] < r and distanceList[1] > r: # 어느 한 점이 행성 외부에 있어 진입/이탈이 필요한 경우
      count += 1
  print(count)
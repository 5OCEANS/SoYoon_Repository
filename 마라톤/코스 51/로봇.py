import sys
input = sys.stdin.readline
M, n = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y, i = 0, 0, 0
flag = 0
for _ in range(n):
  command, ddir = input().split()
  if command == "MOVE":
    d = int(ddir)
    x += (dx[i] * d)
    y += (dy[i] * d)
    if x < 0 or x > M or y < 0 or y > M:
      flag = -1
      break
    else:
      continue
  else:
    mode = int(ddir)
    if mode == 0:
      i = (i + 1) % 4
    else:
      i = (i - 1) % 4

if flag == -1:
  print(-1)
else:
  print(x, y)
import sys
from collections import deque

def bfs(y, x):
  q = deque()
  q.append((y,x))
  graph[y][x] = 0
  while q:
    y, x = q.popleft()
    for dy, dx in d:
      Y, X = y+dy, x+dx
      if (0 <= Y < 10) and (0<= X <10):
        if graph[Y][X] == 'L':
          return graph[y][x]
        if graph[Y][X] == '.':
          q.append((Y, X))
          graph[Y][X] = graph[y][x] + 1

graph = [list(sys.stdin.readline().strip()) for _ in range(10)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(10):
  for j in range(10):
    if graph[i][j] == 'B':
      cnt = bfs(i, j)
print(cnt)
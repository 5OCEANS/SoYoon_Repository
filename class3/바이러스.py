# 틀렸습니다 단방향 연결만을 고려하고 있다고 함.
import sys

comNum = int(sys.stdin.readline()) 
relNum = int(sys.stdin.readline())
list_1 = [1]

for i in range(relNum):
  n, m = map(int, sys.stdin.readline().strip().split())

  if n in list_1:
    if m not in list_1:
      list_1.append(m)
  if m in list_1:
    if n not in list_1:
      list_1.append(n)

print(len(list_1) - 1)


# 양방향, dfs 알고리즘 적용
import sys

comNum = int(sys.stdin.readline()) 
relNum = int(sys.stdin.readline())
graph = [[] for _ in range(comNum + 1)]
visited = [False] * (comNum + 1)

for i in range(relNum):
  n, m = map(int, sys.stdin.readline().strip().split())
  graph[n] += [m]
  graph[m] += [n]

def dfs(node):
  visited[node] = True
  for neighbor in graph[node]:
    if not visited[neighbor]:
      dfs(neighbor)

dfs(1)

print(sum(visited) - 1)

# 양방향, bfs 적용
import sys
from collections import deque

comNum = int(sys.stdin.readline()) 
relNum = int(sys.stdin.readline())
graph = [[] for _ in range(comNum + 1)]
visited = [False] * (comNum + 1)

for i in range(relNum):
  n, m = map(int, sys.stdin.readline().strip().split())
  graph[n] += [m]
  graph[m] += [n]

visited[1] = True
Q = deque([1])

while Q:
  c = Q.popleft()
  for neighbor in graph[c]:
    if not visited[neighbor]:
      Q.append(neighbor)
      visited[neighbor] = True

print(sum(visited) - 1)
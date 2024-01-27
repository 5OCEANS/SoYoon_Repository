# 연결 요소: 그래프의 개수 또는 영역의 개수
# 따라서, DFS 또는 BFS를 수행하는 횟수가 연결 요소의 개수이다.

# DFS 이용
import sys
sys.setrecursionlimit(10**6) # 런타임 에러 발생을 막기 위함
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
  if not visited[i]:
    dfs(graph, i, visited)
    count += 1 # dfs 한 번 끝날 때마다 count + 1

print(count)


# BFS 이용

from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# bfs 함수
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
  if not visited[i]:
    bfs(graph, i, visited)
    count += 1

print(count)
# DFS 풀이
import sys
sys.setrecursionlimit(3000000)

def dfs(node):
  check[node] = 1
  for n in graph[node]:
    if check[n] == 0:
      dfs(n)
            
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
check = [0]*(N+1)
dfs(1)
if 0 in check[1:]:
  for i in range(1, N+1):
    if check[i] == 0:
      print(i)
else:
  print(0)


# BFS 풀이
from collections import deque

def bfs(node):
  q = deque()
  q.append(node)
  check[node] = 1
  while q:
    node = q.popleft()
    for n in graph[node]:
      if check[n] == 0:
        q.append(n)
        check[n] = 1

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
check = [0]*(N+1)
bfs(1)
if 0 in check[1:]:
  for i in range(1, N+1):
    if check[i] == 0:
      print(i)
else:
  print(0)
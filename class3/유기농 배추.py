# BFS로 인접한 1을 0으로 바꿔줌.
# 행렬을 만들어 matrix[x][y] = 1인 경우 BFS로 실행. 한 번 실행될 때마다 cnt += 1
# BFS 함수가 인접한 모든 1을 0으로 바꾸므로 연결된 하나의 블럭 개수를 구할 수 있음.

# 인접한 1개의 영역만 보호할 수 있는 게 아니라 인접한 영역이 1개 있으면 거기에서 또 인접한 상하좌우의 영역을 보호할 수 있다는 게 중요.

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
  queue = [(x, y)]
  matrix[x][y] = 0 # 방문처리

  while queue:
    x, y = queue.pop(0)

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

      if matrix[nx][ny] == 1:
        queue.append((nx, ny))
        matrix[nx][ny] = 0

for i in range(T):
  M, N, K = map(int, input().split())
  matrix = [[0]*(N) for _ in range(M)]
  cnt = 0

  for j in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 1

  for a in range(M):
    for b in range(N):
      if matrix[a][b] == 1:
        BFS(a,b)
        cnt += 1

  print(cnt)

# DFS 풀이
  
import sys
sys.setrecursionlimit(10000) # 런타임에러 발생을 막기 위함

def dfs(x, y):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  # 상, 하, 좌, 우 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < N) and (0 <= ny < M):
      if matrix[nx][ny] == 1:
        matrix[nx][ny] = -1
        dfs(nx, ny)

T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  matrix = [[0]*M for _ in range(N)]
  cnt = 0

  # 행렬 생성
  for _ in range(K):
    m, n = map(int, input().split())
    matrix[n][m] = 1

  for i in range(N): # 행(바깥 리스트)
    for j in range(M): # 열(내부 리스트)
      if matrix[i][j] > 0:
        dfs(i, j)
        cnt += 1 
  
  print(cnt)


from collections import deque
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
queue.append([0,0])
while queue:
  x,y = queue.popleft()
  if board[x][y] == 0:
    continue
  if x == N-1 and y == N-1:
    print("HaruHaru")
    exit()
  if 0 <= x+board[x][y] < N and 0 <= y < N:
    queue.append([x+board[x][y],y])
  if 0 <= x < N and 0 <= y+board[x][y] < N:
    queue.append([x,y+board[x][y]])
print("Hing")

import sys
# DFS를 사용하여 모든 경로를 탐색
def dfs(N, mapList, visited, row, col):
  # 게임판의 경계를 벗어나거나 이미 방문한 경우
  if row < 0 or row >= N or col < 0 or col >= N or visited[row][col]:
    return False
  
  # 현재 위치가 목표 지점인 경우
  if mapList[row][col] == -1:
    return True

  # 현재 칸의 이동값
  jump = mapList[row][col]
  if jump == 0:  # 이동할 수 없는 경우
    return False

  # 현재 위치 방문 처리
  visited[row][col] = True

  # 아래쪽과 오른쪽으로 이동 시도
  if dfs(N, mapList, visited, row + jump, col) or dfs(N, mapList, visited, row, col + jump):
    return True

  return False

# 입력 처리
N = int(sys.stdin.readline())
mapList = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 방문 여부를 기록할 배열
visited = [[False] * N for _ in range(N)]

# DFS 시작
if dfs(N, mapList, visited, 0, 0):
  print("HaruHaru")
else:
  print("Hing")
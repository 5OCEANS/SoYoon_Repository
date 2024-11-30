import sys

N = int(sys.stdin.readline())
plan = list(sys.stdin.readline().strip().split())
location = [1, 1]

for direction in plan:
  if direction == 'L':
    location[1] = (location[1]-1) if location[1] > 1 else 1
    print(location)
  elif direction == 'R':
    location[1] = (location[1]+1) if location[1] < N else N
    print(location)
  elif direction == 'U':
    location[0] = (location[0]-1) if location[0] > 1 else 1  
    print(location)
  elif direction == 'D':
    location[0] = (location[0]+1) if location[0] < N else N
    print(location)

print(location[0], location[1])


# 답안 예시
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)
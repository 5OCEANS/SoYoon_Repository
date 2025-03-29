import sys

while True:
  N = int(sys.stdin.readline())
  if N == 0:
    break

  # 교차 구간의 시작점은 최대값으로, 끝점은 최소값으로 초기화
  x_start, y_start, z_start = -float('inf'), -float('inf'), -float('inf')
  x_end, y_end, z_end = float('inf'), float('inf'), float('inf')

  for _ in range(N):
    x, y, z, d = map(int, sys.stdin.readline().split())
    x_start = max(x_start, x)
    y_start = max(y_start, y)
    z_start = max(z_start, z)
    x_end = min(x_end, x + d)
    y_end = min(y_end, y + d)
    z_end = min(z_end, z + d)

  dx = x_end - x_start
  dy = y_end - y_start
  dz = z_end - z_start

  # 교차 구간이 존재하지 않으면 부피는 0
  if dx <= 0 or dy <= 0 or dz <= 0:
    print(0)
  else:
    print(dx * dy * dz)

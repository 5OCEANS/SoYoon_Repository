import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

seat = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = 0

for i in range(N):
  check = 1
  for j in range(M):
    if seat[i][j] == "0":
      if check >= K:
        result += 1
      check += 1
    else:
      check = 1

print(result)
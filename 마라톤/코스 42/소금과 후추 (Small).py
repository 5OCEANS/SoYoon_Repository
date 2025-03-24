import sys

M, N, K, W = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

B = [[0 for _ in range(N - W + 1)] for _ in range(M - W + 1)]

for i in range(M - W + 1):
  for j in range(N - W + 1):
    window = []
    for x in range(W):
      for y in range(W):
        window.append(A[i + x][j + y])
    window.sort()
    median = window[len(window) // 2]
    B[i][j] = median

for row in B:
  print(' '.join(map(str, row)))
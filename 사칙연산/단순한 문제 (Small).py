import sys

T = int(sys.stdin.readline())

for t in range(T):
  a, b, c = map(int, sys.stdin.readline().split())

  cnt = 0

  for i in range(1, a+1):
    for j in range(1, b+1):
      for k in range(1, c+1):
        if i % j == j % k == k % i:
          cnt += 1

  print(cnt)
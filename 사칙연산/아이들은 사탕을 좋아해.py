import sys

T = int(sys.stdin.readline())

for i in range(T):
  N, K = map(int, sys.stdin.readline().strip().split())
  candyCount = list(map(int, sys.stdin.readline().strip().split()))

  res = 0

  for j in range(N):
    res += (candyCount[j] // K)
  
  print(res)
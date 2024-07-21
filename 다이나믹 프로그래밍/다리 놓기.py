import sys, math

# m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수
# mCn = m! / (m-n)!*n!

T = int(sys.stdin.readline())

for i in range(T):
  N, M = map(int, sys.stdin.readline().strip().split())

  ans = int(math.factorial(M) / (math.factorial(M-N) * math.factorial(N)))

  print(ans)
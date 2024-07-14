import sys    # (n * (n + 1)) // 2 공식 이용

A, B = map(int, sys.stdin.readline().strip().split())

if A > B:
  A, B = B, A

# 1부터 B까지의 합과 1부터 A - 1까지의 합의 차를 출력한다.
print((B * (B + 1) // 2) - (A * (A - 1) // 2))
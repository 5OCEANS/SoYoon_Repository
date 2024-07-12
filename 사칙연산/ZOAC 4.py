import sys, math

H, W, N, M = map(int,sys.stdin.readline().strip().split())

cnt = math.ceil(W / (M + 1)) * math.ceil(H / (N + 1))
print(cnt)
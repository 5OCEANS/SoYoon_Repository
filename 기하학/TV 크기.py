import sys, math

D, H, W = map(int, sys.stdin.readline().strip().split())

K = math.sqrt(D**2 / (H * H + W *  W))

print(math.floor(H*K), math.floor(W*K))
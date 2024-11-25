import sys

N, M = map(int, sys.stdin.readline().strip().split())
numList = [str(i) for i in range(1, N*M+1)]

for i in range(N):
  print(' '.join(numList[i*M:(i+1)*M]))
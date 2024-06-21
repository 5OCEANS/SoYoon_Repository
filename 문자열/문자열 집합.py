import sys

N, M = map(int, sys.stdin.readline().strip().split())

S = []
cnt = 0

for i in range(N):
  string = sys.stdin.readline().strip()
  S.append(string)

S = set(S)

for i in range(M):
  string = sys.stdin.readline().strip()
  if string in S:
    cnt += 1

print(cnt)
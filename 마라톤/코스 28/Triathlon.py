import sys

N = int(sys.stdin.readline().strip())
maxScore = 0
for _ in range(N):
  a, d, g = map(int, sys.stdin.readline().strip().split())
  score = a * (d+g)
  if a == (d+g):
    score *= 2
  if maxScore < score:
    maxScore = score
print(maxScore)
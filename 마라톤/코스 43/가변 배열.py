import sys

s0, N, M = map(int, sys.stdin.readline().strip().split())
maxLen = s0
currentLen = 0

for i in range(N+M):
  num = int(sys.stdin.readline().strip())
  if num == 1: # 원소를 저장
    currentLen += 1
    if currentLen > maxLen:
      maxLen *= 2
  else: # 원소를 삭제
    currentLen -= 1

print(maxLen)
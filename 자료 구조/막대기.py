import sys

N = int(sys.stdin.readline())

max = 0
result = 0
hList = []

for i in range(N):
  h = int(sys.stdin.readline())
  hList.append(h)

for i in range(N):
  if hList[N-1-i] > max:
    result += 1
    max = hList[N-1-i]

print(result)
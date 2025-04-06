import sys

N, M = map(int, sys.stdin.readline().strip().split())

numList = list(map(int, sys.stdin.readline().strip().split()))
mList = list(map(int, sys.stdin.readline().strip().split()))
correct_set = set(mList)

result = [0] * N
for i in range(N):
  if i + 1 in correct_set:
    result[i] = numList[i]

for i in range(N):
  if result[i] == 0:
    for choice in range(1, 6):
      if choice == numList[i]:
        continue
      if i > 0 and result[i - 1] == choice:
        continue
      if i < N - 1 and result[i + 1] == choice and result[i + 1] != 0:
        continue
      result[i] = choice
      break

print(' '.join(map(str, result)))
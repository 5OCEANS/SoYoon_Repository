import sys

N = int(sys.stdin.readline())
numList = []
for _ in range(N):
  num = int(sys.stdin.readline())
  numList.append(num)
numList.sort()

answers = []
for num in numList:
  answers.append(num*N)
  N -= 1
print(max(answers))
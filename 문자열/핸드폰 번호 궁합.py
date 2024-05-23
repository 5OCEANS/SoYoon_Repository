import sys

# 14번 반복해야 함
numList = [0 for _ in range(16)]
resultList = []

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

for i in range(8):
  numList[i*2] = int(A[i])
  numList[i*2+1] = int(B[i])

for i in range(14):
  for j in range(len(numList) - 1):
    num = (numList[j] + numList[j+1]) % 10
    resultList.append(num)
  numList = resultList.copy()
  resultList = []

print(str(numList[0]) + str(numList[1]))
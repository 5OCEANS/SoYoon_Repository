import sys

numCnt = int(sys.stdin.readline())
arr = [0]*10001

for __ in range(numCnt):
  num = int(sys.stdin.readline())
  arr[num] += 1

for i in range(10001):
  if arr[i] != 0:
    for k in range(arr[i]):
      print(i)
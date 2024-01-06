numCnt = int(input())
numList = list(map(int, input()))
hap = 0

for i in range(0, numCnt):
  hap += numList[i]

print(hap)
numCnt = int(input())

numList = list(map(int, input().split()))

primeCnt = 0

for i in range(numCnt):
  isPrime = True
  if numList[i] == 1:
    isPrime = False
    continue
  elif numList[i] == 2:
    isPrime = True
    primeCnt += 1
    continue
  
  for d in range(2, numList[i]):
    if numList[i] % d == 0:
      isPrime = False
      break
  
  if isPrime == True:
    primeCnt += 1

print(primeCnt)  
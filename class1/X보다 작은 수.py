caseCnt, stanNum = map(int, input().split())

numList = list(map(int, input().split()))

for i in range(caseCnt):
  if stanNum > numList[i]:
    print(numList[i], end=' ')
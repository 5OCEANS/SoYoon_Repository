numList = [int(input()) for __ in range(10)]
resultNum = []

for i in range(0, 10):
  resultNum.append(numList[i]%42)

resultCnt = len(list(set(resultNum)))

print(resultCnt)
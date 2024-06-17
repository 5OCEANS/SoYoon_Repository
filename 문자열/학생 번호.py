import sys

N = int(sys.stdin.readline())
numList = []

for i in range(N):
  num = sys.stdin.readline().strip()
  numList.append(num)

index = len(numList[0])-1
cnt = 1

while True:
  formattedNumList = []
  for i in range(N):
    formattedNum = numList[i][index:]
    formattedNumList.append(formattedNum)
  if len(formattedNumList) == len(set(formattedNumList)):
    print(cnt)
    break
  else:
    cnt += 1
    index -= 1

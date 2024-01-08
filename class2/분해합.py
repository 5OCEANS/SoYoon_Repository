num = int(input())
isGet = False

for i in range(0, num):
  numList = list(str(i))
  resNum = i
  for d in range(0, len(numList)):
    resNum += int(numList[d])
  if resNum == num:
    isGet = True
    print(i)
    break

if isGet == False:
  print("0")
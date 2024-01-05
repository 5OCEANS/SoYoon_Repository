numList = [int(input()) for __ in range(3)]

resultNumStr = str(numList[0] * numList[1] * numList[2])

count = []

for i in range(0, 10):
  count.append(resultNumStr.count(str(i)))

for i in range(0, 10):
  print(count[i])
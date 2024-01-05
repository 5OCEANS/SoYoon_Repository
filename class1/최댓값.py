numList = [int(input()) for __ in range(9)]

max = 0
index = 100

for i in numList:
  if max < i:
    max = i
    index = numList.index(i)

print(str(max) + "\n" + str(index+1))
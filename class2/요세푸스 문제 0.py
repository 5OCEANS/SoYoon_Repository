n, k = map(int, input().split())

nList = [n+1 for n in range(n)]

yoseList = []
indexNum = 0

for i in range(n):
  indexNum += k % len(nList) -1
  indexNum %= len(nList)
  yoseList.append(nList[indexNum])
  nList.pop(indexNum)

print("<", end = '')

for i in range(n-1):
  print(yoseList[i], end=', ')

print(yoseList[n-1], end='>')
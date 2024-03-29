import sys

stringList = list(sys.stdin.readline().strip().split())
newStringList = []

for i in stringList:
  newString = ''
  j = 0
  while j < len(i):
    if i[j] not in 'aeiou':
      newString += i[j]
    else:
      newString+= i[j]
      j += 2
    j += 1
  
  newStringList.append(newString)

for i in newStringList:
  print(i, end=' ')

import sys

readyFromIng = ['.', 'o', 'm', 'l', 'n']
ingFromReady = ['o', 'w', 'l', 'n', '.']
seat = ['.', '.', 'o', 'L', 'n']

firstLine = []
nextLine = []

for i in range(5):
  if i == 0:
    firstLine = list(sys.stdin.readline().strip())
  else:
    nextLine.append(sys.stdin.readline().strip())

resultList = []

for i in range(len(firstLine)):
  if firstLine[i] == 'o':
    resultList.append(readyFromIng)
  elif firstLine[i] == '.' and nextLine[0][i] == 'o':
    resultList.append(ingFromReady)
  else:
    resultList.append(seat)

zipResult = list(zip(*resultList))
print(zipResult)

for i in range(len(zipResult)):
  print(''.join(zipResult[i]))


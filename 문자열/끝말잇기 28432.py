import sys

N = int(sys.stdin.readline().strip())
stringList = []

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string)

index = stringList.index('?')

firstString = index - 1
lastString = index + 1

M = int(sys.stdin.readline().strip())
candidateList = []

for i in range(M):
  candidate = sys.stdin.readline().strip()
  candidateList.append(candidate)

if N == 1 and M == 1:
    print(candidateList[0])
elif firstString == -1:
  for i in range(len(candidateList)):
    if candidateList[i] not in set(stringList) and stringList[lastString][0] == candidateList[i][-1]:
      print(candidateList[i])
elif lastString >= len(stringList):
  for i in range(len(candidateList)):
    if candidateList[i] not in set(stringList) and stringList[firstString][-1] == candidateList[i][0]:
      print(candidateList[i])
else:
  for i in range(M):
    string = candidateList[i]
    if candidateList[i] not in set(stringList) and string[0] == stringList[firstString][-1] and string[-1] == stringList[lastString][0]:
      print(string)
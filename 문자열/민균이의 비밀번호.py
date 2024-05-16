import sys

N = int(sys.stdin.readline().strip())

stringList = []

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string)

for i in range(N):
  if stringList[i][::-1] in stringList:
    print(len(stringList[i]), stringList[i][len(stringList[i])//2])
    break
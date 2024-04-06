import sys

N = int(sys.stdin.readline())
stringList = []

for i in range(N):
  string = sys.stdin.readline().rstrip()
  stringList.append(string)

for i in range(N):
  print("%d. %s" %(i+1, stringList[i]))
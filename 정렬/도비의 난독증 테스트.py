import sys

while True:
  try:
    stringList = []
    n = int(sys.stdin.readline())
    if n == 0 :
      break
    for i in range(n):
      string = sys.stdin.readline().strip()
      stringList.append([string.upper(), string])
    stringList.sort()
    print(stringList[0][1])
  except:
    break
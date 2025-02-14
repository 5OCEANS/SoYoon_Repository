import sys

n = int(sys.stdin.readline())
for i in range(n):
  s = int(sys.stdin.readline())
  v = int(sys.stdin.readline())
  o = int(sys.stdin.readline())
  sList = list()
  vList = list()
  oList = list()

  for j in range(s):
    word = sys.stdin.readline().strip()
    sList.append(word)
  for j in range(v):
    word = sys.stdin.readline().strip()
    vList.append(word)
  for j in range(o):
    word = sys.stdin.readline().strip()
    oList.append(word)
  
  stringList = list()

  for j in range(s):
    for k in range(v):
      for f in range(o):
        string = sList[j] + ' ' + vList[k] + ' ' + oList[f] + '.'
        stringList.append(string)
  
  if i > 0:
    print()

  for j in range(s*v*o):
    print(stringList[j])
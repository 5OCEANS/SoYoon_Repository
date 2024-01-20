import sys

t = int(sys.stdin.readline())

for i in range(t):
  typeList = []
  nameList = [0]*30
  case = 1
  n = int(sys.stdin.readline())
  for j in range(n):
    name, type = sys.stdin.readline().strip().split()
    if type not in typeList:
      typeList.append(type)
    index = typeList.index(type)
    nameList[index] += 1
  
  for i in range(len(typeList)):
    case = case * (nameList[i] + 1)
  
  print(case - 1)
import sys

N = int(sys.stdin.readline().strip())
charDict = dict()

for j in range(N):
  string = list(sys.stdin.readline().strip())

  for i in string:
    if i == ' ':
      continue
    elif i not in charDict:
      charDict[i] = 1
    else:
      charDict[i] += 1

for key, val in charDict.items():
  print(key, val)




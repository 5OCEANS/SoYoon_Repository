import sys

stringList = [['' for _ in range(5)] for _ in range(15)] 

for i in range(5):
  string = sys.stdin.readline().strip()
  for j in range(len(string)):
    stringList[j][i] = string[j]

for k in range(15):
  print(''.join(stringList[k]), end ='')
# 시간 초과

import sys

N, kindof = sys.stdin.readline().strip().split()
nameList = []

for i in range(int(N)):
  name = sys.stdin.readline().strip()
  if name not in nameList:
    nameList.append(name)

if kindof == 'Y':
  print(len(nameList))
elif kindof == 'F':
  print(len(nameList)//2)
elif kindof == 'O':
  print(len(nameList)//3)

# 성공

import sys

N, kindof = sys.stdin.readline().strip().split()
nameDic = {}

for i in range(int(N)):
  name = sys.stdin.readline().strip()
  nameDic[name] = ''

nameList = list(nameDic.keys())

if kindof == 'Y':
  print(len(nameList))
elif kindof == 'F':
  print(len(nameList)//2)
elif kindof == 'O':
  print(len(nameList)//3)


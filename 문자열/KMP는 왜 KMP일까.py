import sys

workList = list(sys.stdin.readline().strip().split('-'))

name = ''

for i in workList:
  name += i[0]

print(name)
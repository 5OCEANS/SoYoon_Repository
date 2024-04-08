import sys

string = sys.stdin.readline().strip()

chrList = sys.stdin.readline().strip().split()

for i in chrList:
  string = string.replace(i, i.lower())

print(string)
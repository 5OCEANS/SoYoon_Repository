import sys

word = sys.stdin.readline().strip()

strings = sys.stdin.readlines()
count = 0

for string in strings:
  stringList = list(string.strip().split())
  for i in stringList:
    if word in i:
      count += 1
print(count)
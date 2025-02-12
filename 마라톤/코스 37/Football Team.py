import sys

stringList = sys.stdin.readlines()

for string in stringList:
  string = string.strip().replace('i', '!').replace('e', 'i').replace('!', 'e').replace('I', '!').replace('E', 'I').replace('!', 'E')
  print(string)
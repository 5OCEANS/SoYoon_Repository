import sys

word = sys.stdin.readline().strip()
backwardWord = word[::-1]

if word == backwardWord:
  print(1)
else:
  print(0)
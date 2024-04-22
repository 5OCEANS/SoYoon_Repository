import sys

length = int(sys.stdin.readline())

name = sys.stdin.readline().strip()
score = 0

for i in range(length):
  score += ord(name[i]) - 64

print(score)
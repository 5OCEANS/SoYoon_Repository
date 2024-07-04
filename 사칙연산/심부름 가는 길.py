import sys

totalTime = 0

for i in range(4):
  time = int(sys.stdin.readline())
  totalTime += time

print(totalTime//60)
print(totalTime%60)
import sys

n = int(sys.stdin.readline())
q1Count = 0
q2Count = 0
q3Count = 0
q4Count = 0
axis = 0
for i in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  if x == 0 or y == 0:
    axis += 1
  elif x > 0 and y > 0:
    q1Count += 1
  elif x > 0 and y < 0:
    q4Count += 1
  elif x < 0 and y > 0:
    q2Count += 1
  else:
    q3Count += 1

print('Q1: %d'%(q1Count))
print('Q2: %d'%(q2Count))
print('Q3: %d'%(q3Count))
print('Q4: %d'%(q4Count))
print('AXIS: %d'%(axis))
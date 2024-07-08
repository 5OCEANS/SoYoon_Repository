import sys

n = int(sys.stdin.readline().strip())
changyoung = 100
sangduck = 100

for i in range(n):
  chang, sang = map(int, sys.stdin.readline().strip().split())

  if chang == sang:
    continue
  elif chang < sang:
    changyoung -= sang
  else:
    sangduck -= chang

print(changyoung)
print(sangduck)
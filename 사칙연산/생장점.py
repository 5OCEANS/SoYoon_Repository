import sys

while 1:
  line = list(map(int, sys.stdin.readline().strip().split()))
  if line[0] == 0:
    break
  leaf = 1
  
  for i in range(1, len(line), 2):
    leaf *= line[i]
    leaf -= line[i + 1]

  print(leaf)
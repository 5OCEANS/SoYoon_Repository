import sys

N = int(sys.stdin.readline())
tiles = sys.stdin.readline().strip().split()

counter = {}

for i in range(N):
  tile = tiles[i]
  if tile in counter:
    counter[tile] += 1
  else:
    counter[tile] = 1

  if counter[tile] >= 5:
    print(i + 1)
    break
else:
  print(0)
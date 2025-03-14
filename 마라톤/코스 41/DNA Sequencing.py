import sys

M, F = map(int, sys.stdin.readline().strip().split())
bulls = list()
cows = list()
for i in range(M):
  dna = list(sys.stdin.readline().strip())
  bulls.append(dna)
for i in range(F):
  dna = list(sys.stdin.readline().strip())
  cows.append(dna)

all_bovines = bulls + cows

results = []

for i in range(M):
  result_row = []
  for j in range(F):
    parent1 = bulls[i]
    parent2 = cows[j]
    count = 0
    for k, offspring in enumerate(all_bovines):
      if k == i or k == M + j:
        continue
      possible = True
      for l in range(25):
        if offspring[l] != parent1[l] and offspring[l] != parent2[l]:
          possible = False
          break
      if possible:
        count += 1
    result_row.append(count)
  results.append(result_row)

for row in results:
  print(' '.join(map(str, row)))
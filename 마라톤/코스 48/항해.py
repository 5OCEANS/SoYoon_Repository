import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

meals = 0
waste = 0

for length in A:
  max_piece = length // X
  best_waste = float('inf')
  best_meal = 0
  for cnt in range(max_piece, 0, -1):
    min_cut = cnt * X
    max_cut = cnt * Y
    if min_cut <= length:
      if length <= max_cut:
        leftover = 0
      else:
        leftover = length - max_cut
      if leftover < X:
        if leftover < best_waste:
          best_waste = leftover
          best_meal = cnt
  if best_meal == 0:
    if length < X:
      waste += length
  else:
    meals += best_meal
    waste += best_waste

print(meals)
print(waste)
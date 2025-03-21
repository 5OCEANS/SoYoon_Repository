import sys
from itertools import combinations

N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

def generate_numbers(N, cnt):
  result = []
  for ones in combinations(range(N), cnt):
    num = 0
    for i in ones:
      num |= (1 << i)
    result.append(num)
  return result

x_list = generate_numbers(N, a)
y_list = generate_numbers(N, b)

max_xor = 0
for x in x_list:
  for y in y_list:
    max_xor = max(max_xor, x ^ y)

print(max_xor)
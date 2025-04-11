import sys

num_string =int( sys.stdin.readline().strip())
seen = set()
count = 0
current = f"{num_string:04d}"

while current not in seen:
  seen.add(current)
  min_two_digits = current[1:3]
  mid_value = int(min_two_digits)
  squared = mid_value ** 2
  current = f"{squared:04d}"
  count += 1

print(count)
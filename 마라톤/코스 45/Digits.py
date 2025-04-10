import sys

while True:
  line = sys.stdin.readline().strip()
  if line == "END":
    break

  count = 1
  current = line
  while True:
    next_val = str(len(current))
    if next_val == current:
      print(count)
      break
    current = next_val
    count += 1
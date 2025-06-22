import sys
import math

direction_map = {
  "N":  (0, 1),
  "NE": (math.sqrt(0.5), math.sqrt(0.5)),
  "E":  (1, 0),
  "SE": (math.sqrt(0.5), -math.sqrt(0.5)),
  "S":  (0, -1),
  "SW": (-math.sqrt(0.5), -math.sqrt(0.5)),
  "W":  (-1, 0),
  "NW": (-math.sqrt(0.5), math.sqrt(0.5)),
}

case_number = 1

while True:
  line = sys.stdin.readline().strip()
  if line == "END":
    break

  x = 0.0
  y = 0.0
  route = line[:-1].split(',')

  for item in route:
    num = ''
    for i in range(len(item)):
      if item[i].isdigit():
        num += item[i]
      else:
        break
    length = int(num)
    direction = item[len(num):]
    dx, dy = direction_map[direction]
    x += length * dx
    y += length * dy

  distance = math.sqrt(x * x + y * y)
  print(f"You can go to ({x:.3f},{y:.3f}), the distance is {distance:.3f} steps.")
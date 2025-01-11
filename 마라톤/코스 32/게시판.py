import sys

def calculate_visible_area(x1, y1, x2, y2, x3, y3, x4, y4):
  original_area = (x2 - x1) * (y2 - y1)

  overlap_x1 = max(x1, x3)
  overlap_y1 = max(y1, y3)
  overlap_x2 = min(x2, x4)
  overlap_y2 = min(y2, y4)

  if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
    overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)
  else:
    overlap_area = 0

  visible_area = original_area - overlap_area
  return visible_area

t = int(sys.stdin.readline().strip())
for _ in range(t):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())
  print(calculate_visible_area(x1, y1, x2, y2, x3, y3, x4, y4))
import sys

def is_in_the_link(W, H, X, Y, x, y):
  # 직사각형 안에 있는지
  if X <= x <= X + W and Y <= y <= Y + H:
    return 1
  # 왼쪽 반원 안에 있는지
  left_circle_center = (X, Y + (H/2))
  if ((left_circle_center[0]-x)**2 + (left_circle_center[1]-y)**2) <= (H/2)**2:
    return 1
  # 오른쪽 반원 안에 있는지
  right_circle_center = (X + W, Y + (H/2))
  if ((right_circle_center[0]-x)**2 + (right_circle_center[1]-y)**2) <= (H/2)**2:
    return 1
  return 0

W, H, X, Y, P = map(int, sys.stdin.readline().strip().split())
count = 0

for i in range(P):
  x, y = map(int, sys.stdin.readline().strip().split())

  count += is_in_the_link(W, H, X, Y, x, y)

print(count)
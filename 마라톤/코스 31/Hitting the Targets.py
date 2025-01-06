import sys, math

def if_target_rectangle(x1, y1, x2, y2, shotX, shotY):
  if x1 <= shotX <= x2 and y1 <= shotY <= y2:
    return True
  else:
    return False

def if_target_circle(x, y, r, shotX, shotY):
  if math.sqrt((x-shotX)**2 + (y-shotY)**2) <= r:
    return True
  else:
    return False
  
def count_shot_hits(targetList, x, y):
  count = 0
  for target in targetList:
    if target[0] == 'rectangle':
      if if_target_rectangle(int(target[1]), int(target[2]), int(target[3]), int(target[4]), x, y):
        count += 1
    else:
      if if_target_circle(int(target[1]), int(target[2]), int(target[3]), x, y):
        count += 1
  return count

m = int(sys.stdin.readline())
targetList = list()
for i in range(m):
  targetInfo = list(sys.stdin.readline().strip().split())
  targetList.append(targetInfo)

n = int(sys.stdin.readline().strip())
for i in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  ans = count_shot_hits(targetList, x, y)
  print(ans)
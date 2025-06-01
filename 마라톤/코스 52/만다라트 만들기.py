import sys
input = sys.stdin.readline

table = [] 
for _ in range(9):
  table.append(list(input().split()))
mid_goal = []
for i in range(1, 9, 3):
  for j in range(1, 9, 3):
    if i != 4 or j != 4:
      mid_goal.append([table[i][j], i, j])
mid_goal.sort()
for i in range(8):
  goal, y, x = mid_goal[i]
  print('#%d. %s' % (i + 1, goal))
  detail_goal = []
  for j in range(y - 1, y + 2):
    for k in range(x - 1, x + 2):
      if j != y or k != x:
        detail_goal.append([table[j][k], j, k])
  detail_goal.sort() 
  for j in range(8):
    print('#%d-%d. %s' % (i + 1, j + 1, detail_goal[j][0]))
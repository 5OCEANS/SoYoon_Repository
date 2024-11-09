import sys

T = int(sys.stdin.readline())

for _ in range(T):
  dotList = []
  for _ in range(4):
    dot = tuple(map(int, sys.stdin.readline().strip().split()))
    dotList.append(dot)
  
  sortedDotList = sorted(dotList, key= lambda x:(x[0], x[1]))
  
  diagonal_distance1 = (sortedDotList[0][0] - sortedDotList[3][0])**2 + (sortedDotList[0][1] - sortedDotList[3][1])**2
  diagonal_distance2 = (sortedDotList[1][0] - sortedDotList[2][0])**2 + (sortedDotList[1][1] - sortedDotList[2][1])**2

  line1 = (sortedDotList[0][0] - sortedDotList[1][0])**2 + (sortedDotList[0][1] - sortedDotList[1][1])**2
  line2 = (sortedDotList[1][0] - sortedDotList[3][0])**2 + (sortedDotList[1][1] - sortedDotList[3][1])**2
  line3 = (sortedDotList[2][0] - sortedDotList[3][0])**2 + (sortedDotList[2][1] - sortedDotList[3][1])**2
  line4 = (sortedDotList[0][0] - sortedDotList[2][0])**2 + (sortedDotList[0][1] - sortedDotList[2][1])**2

  if diagonal_distance1 == diagonal_distance2 and line1 == line2 == line3 == line4:
    print(1)
  else:
    print(0)
import sys

for i in range(3):
  max = 0
  cnt = 1

  numString = sys.stdin.readline().strip()

  for j in range(7):
    if numString[j] == numString[j+1]:
      cnt += 1
    else:
      if max < cnt:
        max = cnt
      cnt = 1
  
  # 마지막 숫자까지 연속적일 경우도 고려해야 함. ex) 12355555 -> 5
  if max < cnt:
    max = cnt

  print(max)
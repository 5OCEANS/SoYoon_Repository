import sys

T = int(sys.stdin.readline())
for i in range(T):
  p, q, r = sys.stdin.readline().strip().split()
  for j in range(2, 17):
    try:
      transP = int(p, j)
      transQ = int(q, j)
      transR = int(r, j)
      if transR == (transP * transQ):
        print(j)
        break
    except ValueError: # 숫자가 j보다 크면 오류 발생
      continue
  else:
    print(0)
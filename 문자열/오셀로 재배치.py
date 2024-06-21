import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())

  earlyString = sys.stdin.readline().strip()
  targetString = sys.stdin.readline().strip()

  # W: 3 B: 2, B로 바뀌어야 하는 것: 1, W로 바뀌어야 하는 것: 1
  # W: 0 B: 7, B로 바뀌어야 하는 것: 0, W로 바뀌어야 하는 것: 3
  # W: 2 B: 2, B로 바뀌어야 하는 것: 2, W로 바뀌어야 하는 것: 1

  haveToB = 0
  haveToW = 0

  for j in range(N):
    if earlyString[j] != targetString[j]:
      if targetString[j] == 'B':
        haveToB += 1
      elif targetString[j] == 'W':
        haveToW += 1
    else:
      continue

  method1 = min(haveToB, haveToW)
  method2 = max(haveToB, haveToW) - method1

  print(method1 + method2)
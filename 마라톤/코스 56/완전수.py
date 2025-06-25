import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for s in numbers:
  tmp = []
  for i in range(1, (s + 1) // 2 + 1):
    if s % i == 0:
      if s // i == i:
        tmp.append(i)
      else:
        tmp.append(i)
        if i != s // i and s // i != s:
          tmp.append(s // i)
  ans = sum(sorted(set(tmp))) - s
  if ans > s:
    print("Abundant")
  elif ans == s:
    print("Perfect")
  else:
    print("Deficient")

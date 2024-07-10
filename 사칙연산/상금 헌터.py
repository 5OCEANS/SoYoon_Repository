import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  a, b = map(int, sys.stdin.readline().strip().split())
  ans = 0
  
  if a == 1:
    ans += 5000000
  elif a > 1 and a < 4:
    ans += 3000000
  elif a >= 4 and a < 7:
    ans += 2000000
  elif a >= 7 and a < 11:
    ans += 500000
  elif a >= 11 and a < 16:
    ans += 300000
  elif a >= 16 and a < 22:
    ans += 100000
  else:
    ans += 0
  
  if b == 1:
    ans += 5120000
  elif b > 1 and b < 4:
    ans += 2560000
  elif b >= 4 and b < 8:
    ans += 1280000
  elif b >= 8 and b < 16:
    ans += 640000
  elif b >= 16 and b < 32:
    ans += 320000
  else:
    ans += 0
  
  print(ans)
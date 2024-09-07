import sys, math

T = int(sys.stdin.readline())

for i in range(T):
  a, b = map(int, sys.stdin.readline().strip().split())

  lcm = math.lcm(a, b)
  gcd = math.gcd(a, b)
  
  print(lcm, gcd)
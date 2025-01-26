import sys, math

n = int(sys.stdin.readline())  
total_elevation = 0  

for _ in range(n):
  a, d = map(int, sys.stdin.readline().strip().split())  
  elevation_change = d * math.sin(math.radians(a))
  total_elevation += elevation_change

print(f"{total_elevation:.2f}")
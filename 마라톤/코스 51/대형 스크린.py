import sys, math

rh, rv, sh, sv = map(int, sys.stdin.readline().strip().split())
n = int(sys.stdin.readline().strip())
min_price = 1000000000
for i in range(n):
  rhi, rvi, shi, svi, pi = map(int, sys.stdin.readline().strip().split())
  horizontal = max(math.ceil(rh / rhi), math.ceil(sh / shi))
  vertical = max(math.ceil(rv / rvi), math.ceil(sv / svi))
  min_price = min(min_price, horizontal * vertical * pi)

  horizontal = max(math.ceil(rh / rvi), math.ceil(sh / svi))
  vertical = max(math.ceil(rv / rhi), math.ceil(sv / shi))
  min_price = min(min_price, horizontal * vertical * pi)
print(min_price)
import sys
from decimal import Decimal, ROUND_FLOOR

N = int(sys.stdin.readline().strip())
initial = (Decimal(sys.stdin.readline().strip()[1:]) * 100).quantize(Decimal("1"), rounding=ROUND_FLOOR)
ans = 0

for _ in range(N):
  money = (Decimal(sys.stdin.readline().strip()[1:]) * 100).quantize(Decimal("1"), rounding=ROUND_FLOOR)
  initial += money
  if initial % 100 != 0:
    ans += 1

print(ans)
n, m = map(int, input().split())
money = list(map(int, input().split()))

sum_value = sum(money[0:m])
ans = sum_value

for st in range(n - m):
  sum_value -= money[st]
  sum_value += money[st + m]
  ans = max(ans, sum_value)

print(ans)
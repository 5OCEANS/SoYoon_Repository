h, m = map(int, input().split())

if m >= 45:
  m -= 45
elif m < 45:
  if h < 1:
    h = 23
  else:
    h -= 1
  m = 60 + (m - 45)

print(h, m)
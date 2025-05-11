import sys

x_str, y_str = sys.stdin.readline().split()
x = float(x_str)
y = float(y_str)

n = int(sys.stdin.readline())
shields = []

for _ in range(n):
  li_str, ui_str, fi_str = sys.stdin.readline().split()
  li = int(li_str)
  ui = int(ui_str)
  fi = float(fi_str)
  shields.append((li, ui, fi))

shields.sort()
contribution = 0.0
prev = 0

for li, ui, fi in shields:
  if li > prev:
    contribution += (li - prev) * 1.0
  contribution += (ui - li) * fi
  prev = ui

if prev < y:
  contribution += (y - prev) * 1.0

v = x / contribution
print(f"{v:.10f}")
import sys

while True:
  try:
    line = sys.stdin.readline().strip()

    if line == "0 0 0":
      break

    n, m, k = map(int, line.split())
    indep = n - m - k
    need = n // 2 + 1

    if m >= need:
      print(0)
    elif m + indep < need:
      print(-1)
    else:
      print(need - m)
  except:
    break
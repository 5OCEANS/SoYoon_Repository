import sys

N = int(sys.stdin.readline())

ans = 0

for i in range(2023, N + 1):
  x = str(i)

  if not {'2', '3', '0'}.issubset(set(x)): # 0, 2, 3 원소가 문자열에 있는지. 하위 집합인지 물어보는 것.
    continue
  
  tmp = []

  for j in x:
    if j == '2' and len(tmp) in [0, 2]:
      tmp.append(j)
    elif j == '0' and len(tmp) == 1:
      tmp.append(j)
    elif j == '3' and len(tmp) == 3:
      ans += 1
      break

print(ans)
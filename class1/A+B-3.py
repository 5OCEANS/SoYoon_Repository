caseCnt = int(input())
result = []

for i in range(0, caseCnt):
  a, b = map(int, input().split())
  result.append(a+b)

for i in range(0, caseCnt):
  print(result[i])
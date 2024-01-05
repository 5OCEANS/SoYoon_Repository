caseCnt = int(input())
result = []

for i in range(1, caseCnt+1):
  cnt, str = input().split()
  eachStr = list(str) # ['A', 'B', 'C']
  for d in range(0, len(eachStr)): 
    eachStr[d] = eachStr[d] * int(cnt)
  result.append(''.join(eachStr))

for i in result:
  print(i)
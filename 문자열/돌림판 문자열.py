import sys

N = int(sys.stdin.readline())

alpabet = sys.stdin.readline().strip()

index = N - 1

M = int(sys.stdin.readline())

S = sys.stdin.readline().strip()

result = 0

for i in range(M):
  string = alpabet[index:] + alpabet[0:index]
  if string.find(S[i]) != -1:
    if string.find(S[i]) != 0:
      num = string.find(S[i]) 
    else:
      num = string.find(S[i], 1) if string.find(S[i], 1) != -1 else N
  else:
    print(-1)
    break
  result += num
  index = (num + index) % N
else:
  print(result)
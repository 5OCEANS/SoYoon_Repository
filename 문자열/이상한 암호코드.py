import sys

S, K = sys.stdin.readline().strip().split()

S = S.lower()

K = int(K)

ans = ''
ans += S[0]

numList = []
ansList = []

for i in range(1, len(S)):
  if S[i-1] == S[i]:
    ans += S[i]
  else:
    if len(ans) >= K and S[i-1] not in numList:
      ansList.append('1')
      numList.append(S[i-1])
      ans = ''
      ans += S[i]
    elif len(ans) < K and S[i-1] not in numList:
      ansList.append('0')
      numList.append(S[i-1])
      ans = ''
      ans += S[i]

if len(ans) >= K and S[-1] not in numList:
  ansList.append('1')
elif len(ans) < K and S[-1] not in numList:
  ansList.append('0')

print(''.join(ansList))
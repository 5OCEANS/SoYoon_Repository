# 틀렸습니다.

import sys

alphaDic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J':0, 'K': 0,
            'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
            'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

string = sys.stdin.readline().strip()
cnt = 0

for i in range(len(string)):
  if alphaDic[string[i]] == 0:
    if sum(list(alphaDic.values())) != 0:
      cnt += sum(list(alphaDic.values()))

    alphaDic[string[i]] = 1

  else: 
    alphaDic[string[i]] = 0
  

print(cnt//2)


# 성공

import sys
S = sys.stdin.readline().strip()
result = 0 
for start in range(52):
  for end in range(start+1,52):
    if S[start] == S[end]: 
      cows = S[start:end+1] 
      for i in cows:
        if cows.count(i) == 1: 
          result += 1
      break
print(result // 2) 
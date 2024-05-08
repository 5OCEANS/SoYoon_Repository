T = int(input())

X = {'A': '000000', 'B': '001111', 'C': '010011', 'D': '011100',
      'E': '100110', 'F': '101001', 'G': '110101', 'H': '111010'}

M = input()

val = list(X.values()) # 000000 과 같은 값들을 리스트로 모아놓음
key = list(X.keys())   # A B 와 같은 키들을 리스트로 모아놓음
ans = []
c = 0

for i in range(0, len(M), 6):
  a = M[i:i+6]
  c += 1
  if a in val: # 값들 중에서 완벽히 일치하는 values가 있다면
    for j in range(8):
      if a == val[j]:
        ans.append(key[j]) # 해당하는 인덱스의 키를 넣어줌.
  else:
    ct = 0 # 다른 values 개수
    for t in range(8):
      cnt = 0 # 다른 스펠링 개수
      for j in range(6):
        if a[j] != val[t][j]:
          cnt += 1
      if cnt <= 1: # 한 자리만 틀린 경우
        ans.append(key[t])
        break
      else:
        ct += 1 # 두 자리 이상 틀린 경우
    if ct == 8: # A ~ H와 비교했을 때, 모두 두 자리 이상 틀린 경우
      break

if len(ans) == T:
  print(''.join(ans))
else:
  print(c)
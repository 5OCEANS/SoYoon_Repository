# 브루트포스 알고리즘

import sys

N = int(sys.stdin.readline())

sent = sys.stdin.readline().strip()

ans = ''

for i in range(1, N):
  a = sent[:i] # 앞에서부터 1칸씩
  r = sent[::-1]
  b = r[:i][::-1] # 뒤에서부터 1칸씩

  check = 0
  
  for j in range(len(a)):
    if a[j] != b[j]:
      check += 1
    
  if check == 1: # 단 1개만 다르다면
    ans = 'YES'
    break

if ans != 'YES':
  ans = 'NO'

print(ans)
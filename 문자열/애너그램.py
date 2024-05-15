import sys

T = int(sys.stdin.readline())

for i in range(T):
  A, B = map(list, sys.stdin.readline().strip().split())
  removeB = B.copy()

  if len(A) != len(B):
    print(''.join(A), '&', ''.join(B), 'are NOT anagrams.')
    continue
  
  for i in A:
    if i in removeB:
      removeB.remove(i)
    else:
      print(''.join(A), '&', ''.join(B), 'are NOT anagrams.')
      break
  else:
    print(''.join(A), '&', ''.join(B), 'are anagrams.')
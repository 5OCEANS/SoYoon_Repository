import sys

N = int(sys.stdin.readline())

sing = ['baby', 'sukhwan', 'tururu', 'turu', 
        'very', 'cute', 'tururu', 'turu',
        'in', 'bed', 'tururu', 'turu',
        'baby', 'sukhwan']

# 14개고 인덱스가 2, 3, 6, 7, 10, 11일 때 ru를 계속 추가함

if ((N%14)-1) in [2, 6, 10]:
  if N//14 >= 3:
    print('tu+ru*'+str(N//14 + 2))
  else:
    print(sing[(N%14) -1] + 'ru' * (N//14))

elif ((N%14)-1) in [3, 7, 11]:
  if N//14 >= 4:
    print('tu+ru*'+str(N//14+1))
  else:
    print(sing[(N%14) -1] + 'ru' * (N//14))

else:
  print(sing[((N%14) -1)])
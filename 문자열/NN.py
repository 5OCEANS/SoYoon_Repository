# 출력 초과 

# import sys

# N, M = sys.stdin.readline().strip().split()

# if int(N) > int(M):
#   if len(N) % int(M) == 0:
#     mul = int(M) // len(N)
#   else:
#     mul = int(M) // len(N) + 1

#     N = N * mul

#   for i in range(int(M)):
#     print(N[i], end = '')

# else:
#   for i in range(int(N)):
#     print(N, end ='')

# 성공

import sys

N, M= map(int, sys.stdin.readline().split())
print((str(N)*N)[:M])
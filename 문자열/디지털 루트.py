# 틀렸습니다.

# import sys

# while True:
#   try:

#     N = sys.stdin.readline().strip()

#     if int(N) == 0:
#       break

#     if len(N) == 1:
#       print(N)
    
#     while True:
#       sum = 0
#       for i in N:
#         sum += int(i)
      
#       if len(str(sum)) == 1:
#         print(sum)
#         break

#       N = str(sum)


#   except:
#     break


while True :
  N = int(input())
  if N == 0 : break
  ans = N
  while ans >= 10 :
    tmp = 0
    while ans > 0 :
      tmp += ans % 10
      ans //= 10
    ans = tmp
  print(ans)
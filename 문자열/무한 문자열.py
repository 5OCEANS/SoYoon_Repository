import math

# 입력
a=input()
b=input()

# 길이 재기
al=len(a)
bl=len(b)

# 최소공배수를 찾음
c=math.lcm(al,bl)

# 최소공배수에서 길이만큼 나눠서 몇배를 해야 하는지를 찾음
al=c//al
bl=c//bl

# 각각을 곱해서 같은 형태가 되는지를 확인함
if a*al==b*bl:
  print(1)
else:
  print(0)
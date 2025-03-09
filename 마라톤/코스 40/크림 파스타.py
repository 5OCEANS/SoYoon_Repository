from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

d = [0]*N
min_value = A[0]
for i in range(1,N):
  min_value = min(min_value,A[i])
  d[i] = max(d[i-1],A[i]-min_value)

print(*d)
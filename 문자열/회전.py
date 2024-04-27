import sys

N = sys.stdin.readline().strip()
result = 0

for i in range(len(N)):
  num = int(N[i:len(N)] + N[0:i])
  print(num)
  result += num

print(result)


# 12345    0  5   0  0 
# 2345 1   1  5   0  1
# 345 12   2  5   0  2
# 45 123   3  5   0  3
# 5 1234   4  5   0  4
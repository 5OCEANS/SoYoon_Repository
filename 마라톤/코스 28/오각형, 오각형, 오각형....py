import sys

N = int(sys.stdin.readline())
ans = N*5 + ((N-1)*(2*2+(N-2)*3)//2)
print(ans%45678)

# 1 - 5
# 2 - 10 + 2
# 3 - 15 + 5 + 2
# 4 - 20 + 8 + 5 + 2


# a = 2
# d = 3
# l = (a+(n-1)*d)
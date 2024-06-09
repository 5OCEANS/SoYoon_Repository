import sys, math

n, m = map(int, sys.stdin.readline().strip().split(':'))

gcd = math.gcd(n, m)

print(str(n//gcd)+':'+str(m//gcd))
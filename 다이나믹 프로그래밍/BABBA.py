import sys

K = int(sys.stdin.readline().strip())

aCnt = 1
aCntPlusOne = 0
bCnt = 0
bCntPlusOne = 1


# A               1 0     1
# B               0 1     2
# BA              1 1     3
# BAB             1 2     4
# BABBA           2 3     5
# BABBABAB        3 5     6
# BABBABABBABBA   5 8     7

# A -> B      1 0 -> 0 1
# B -> B A    0 1 -> 1 1

# 피보나치 수열 공식 

for i in range(K):
  aCnt, aCntPlusOne = aCntPlusOne, aCnt + aCntPlusOne
  bCnt, bCntPlusOne = bCntPlusOne, bCnt + bCntPlusOne

print(aCnt, bCnt)



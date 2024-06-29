import sys

S = sys.stdin.readline().strip()

for i in range(len(S)):
  if S[i:] == S[i:][::-1]:
    palindrome = S + S[:i][::-1]
    print(len(palindrome))
    break

# abab
# abab == baba
# bab == bab ababa

# abacaba
# abacaba == abacaba abacaba

# qwerty
# qwerty == ytrewq
# werty == ytrew
# erty == ytre
# rty == ytr
# ty == yt
# y == y qwertytrewq
import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()
vowel = 0
vowel += b.count('a')
vowel += b.count('i')
vowel += b.count('u')
vowel += b.count('e')
vowel += b.count('o')
print(vowel)
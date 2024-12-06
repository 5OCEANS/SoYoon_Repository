import sys

string = sys.stdin.readline().strip()
vowel = 0

vowel += string.count('a')
vowel += string.count('e')
vowel += string.count('i')
vowel += string.count('o')
vowel += string.count('u')

print(vowel)
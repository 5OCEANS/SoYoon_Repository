import sys

def is_palindrome(s):
  return s == s[::-1]

def make_palindrome_by_deleting_one_char(s):
  for i in range(len(s)):
    temp = s[:i] + s[i+1:]
    if is_palindrome(temp):
      return temp
  return "not possible"

while True:
  line = sys.stdin.readline().strip()
  if line == "#":
    break
  result = make_palindrome_by_deleting_one_char(line)
  print(result)
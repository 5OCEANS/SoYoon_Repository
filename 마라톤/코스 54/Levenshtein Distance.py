import sys

alphabet = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
result = set()

for i in range(len(s) + 1):
  for c in alphabet:
    new_str = s[:i] + c + s[i:]
    result.add(new_str)

for i in range(len(s)):
  new_str = s[:i] + s[i+1:]
  result.add(new_str)

for i in range(len(s)):
  for c in alphabet:
    if s[i] != c:
      new_str = s[:i] + c + s[i+1:]
      result.add(new_str)

if s in result:
  result.remove(s)

for word in sorted(result):
  print(word)
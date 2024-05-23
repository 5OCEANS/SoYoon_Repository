import sys

string = sys.stdin.readline().strip()
result = 0

# 한글자여서 아무것도 없고 + 자기 자신 알파벳 순서
# 두글자이고 첫번째 글자가 A라서 26 * 1 + 자기 자신 알파벳 순서
# 두글자이고 첫번째 글자가 B라서 26 * 2 + 자기 자신 알파벳 순서
# 세글자라면? 

string = string[::-1]

for i in range(len(string)):
  result += pow(26, i) * (ord(string[i]) - 64)

print(result)
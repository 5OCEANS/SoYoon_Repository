# import sys

# # T = sys.stdin.readline().strip()

# # U -> C

# # chr(ord(U) ^ key) = C

# # ord(U) ^ key = 67

# # 01000011

# # s d s s s s d d

# 주어진 문자열 S 입력 받기
encrypted_string = input()

# "CHICKENS"와 주어진 문자열의 처음 8글자를 XOR 연산하여 추출된 key 값 찾기 ->  XOR 연산의 특성 상, 동일한 값에 두 번 XOR 연산을 수행하면 초기 값으로 돌아감.
keyword = "CHICKENS"
key = ""
for i in range(8):
  key += chr(ord(encrypted_string[i]) ^ ord(keyword[i]))

# key를 사용하여 전체 문자열을 XOR 연산하여 복호화
original_string = ""
for i in range(len(encrypted_string)):
  original_string += chr(ord(encrypted_string[i]) ^ ord(key[i % 8]))

print(original_string)
string = input()

# 사전순으로 가장 큰 수를 미리 입력
answer = "z" * len(string)

# 세 단어로 나누기 위해서 두 번을 자름
# 시간 복잡도: O(n^2)
for i in range(1, len(string) - 1):
  for j in range(i + 1, len(string)):
    s1 = string[:i][::-1]
    s2 = string[i:j][::-1]
    s3 = string[j:][::-1]
    new_string = s1 + s2 + s3
    answer = min(answer, new_string)  # 사전순으로 더 앞선 수를 가져옴

print(answer)
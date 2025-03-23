import sys

n = int(sys.stdin.readline())
opus_numbers = list(map(int, sys.stdin.readline().split()))

# 교수들의 번호와 opus 번호를 함께 저장
# 초기 교수 번호는 1부터 시작
line = list(enumerate(opus_numbers, start=1))

current_index = 0

while len(line) > 1:
  k = line[current_index][1]  # 현재 교수의 opus 번호
  # 제거할 교수의 인덱스 계산
  remove_index = (current_index + k - 1) % len(line)
  # 교수 제거
  line.pop(remove_index)
  # 다음 시작 인덱스 설정
  current_index = remove_index % len(line)

# 마지막 남은 교수의 번호 출력
print(line[0][0])
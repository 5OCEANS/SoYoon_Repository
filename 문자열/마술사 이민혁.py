import sys

R, C = map(int, sys.stdin.readline().split())

leftTop = []

for i in range(R):
  string = list(sys.stdin.readline().strip())
  leftTop.append(string)

A, B = map(int, sys.stdin.readline().split())

for i in range(R):
  leftTop[i] = leftTop[i] + leftTop[i][::-1]

# for i in range(R):                # 같은 주소를 참조해 값 하나가 변경되면 다른 리스트에도 영향을 미침. -> 실패
#   leftTop.append(leftTop[R-i-1])

for i in range(R):                  # 방법 1
  leftTop.append(leftTop[R-i-1].copy())

# for i in range(R-1, -1, -1):      # 방법 2
#   leftTop.append(leftTop[i][::-1])

leftTop[A-1][B-1] = '#' if leftTop[A-1][B-1] == '.' else '.'

for i in range(2*R):
  print(''.join(leftTop[i]))
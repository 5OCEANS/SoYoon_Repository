import sys

# 유니코드 값 = 44032 + 초성번호 * 21 * 28 + 중성번호 * 28 + 종성번호

CHO_MAP = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"

S = sys.stdin.readline().strip()

for i in S:
  t = ord(i) - 44032
  print(CHO_MAP[t//21//28], end = '')
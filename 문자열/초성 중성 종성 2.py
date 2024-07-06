import sys

# 유니코드 값 = 44032 + 초성번호 * 21 * 28 + 중성번호 * 28 + 종성번호

CHO_MAP = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG_MAP = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG_MAP = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

initial = CHO_MAP.index(sys.stdin.readline().strip())
neuter = JUNG_MAP.index(sys.stdin.readline().strip())
final = JONG_MAP.index(input() or ' ')

print(chr(44032 + initial*21*28 + neuter * 28 + final))
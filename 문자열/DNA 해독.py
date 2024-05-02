# 시간 초과

# import sys

# N = int(sys.stdin.readline().strip())

# DNA = sys.stdin.readline().strip()

# for i in range(N):
#   an_1 = DNA[len(DNA) - 2]
#   an = DNA[len(DNA) - 1]

#   decoding = ''

#   if an_1 == 'A':
#     if an == 'A' or an == 'C':
#       decoding = 'A'
#     elif an == 'G':
#       decoding = 'C'
#     elif an == 'T':
#       decoding = 'G'
#   elif an_1 == 'G':
#     if an == 'A':
#       decoding = 'C'
#     elif an == 'G':
#       decoding = 'G'
#     elif an == 'C':
#       decoding = 'T'
#     elif an == 'T':
#       decoding = 'A'
#   elif an_1 == 'C':
#     if an == 'A':
#       decoding = 'A'
#     elif an == 'G':
#       decoding = 'T'
#     elif an == 'C':
#       decoding = 'C'
#     elif an == 'T':
#       decoding = 'G'
#   elif an_1 == 'T':
#     if an == 'A':
#       decoding = 'G'
#     elif an == 'G':
#       decoding = 'A'
#     elif an == 'C':
#       decoding = 'G'
#     elif an == 'T':
#       decoding = 'T'
  
#   DNA = DNA[:len(DNA)-2] + decoding

# print(DNA)

n = int(input())

s = list(input())

# 표의 내용을 딕셔너리로 선언

dna = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
      "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
      "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

while True:

  if len(s) == 1: # 문자열의 길이가 1이 될 때까지
    break

  ss = s[-2] + s[-1]

  if ss in dna:
    del s[-2:]            # 해당 내용 삭제

    s.append(dna.get(ss)) # 딕셔너리의 get을 통해 해당 문자열에 해당하는 value 값을 가져옴.

print(*s) # 리스트 요소를 한번에 출력
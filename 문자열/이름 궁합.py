import sys

alphaDic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J':2, 'K': 2,
            'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1,
            'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

stringList = ['' for _ in range(len(A)*2)]

for i in range(len(A)):
  stringList[i*2] = alphaDic[A[i]]
  stringList[i*2+1] = alphaDic[B[i]]

while len(stringList) > 2:
  newStringList = []
  for i in range(len(stringList) - 1):
    newStringList.append((stringList[i] + stringList[i+1])%10)
  
  stringList = newStringList

print(str(stringList[0])+str(stringList[1]))


# ABC
# DEF

# A D B E C F
# (A+D) (D+B) (B+E) (E+C) (C+F)
# (A+2D+B) () () ()
# () () ()
# () ()
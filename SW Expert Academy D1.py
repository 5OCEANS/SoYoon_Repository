import sys

num = int(sys.stdin.readline())
numList = [0]*10
while True:
    numInt = num % 10
    numList[numInt] += 1
    num = num // 10
    if num < 1:
        break
print('0 1 2 3 4 5 6 7 8 9')
for i in numList:
    print(i, end=' ')



inch = float(input())
cm = inch * 2.54
print("%0.2f inch => %0.2f cm" %(inch, cm))


while True:
  try:
    sentence = input()
    if sentence == '':
      break
    sentence = sentence.upper()
    print('>>', sentence)
  except:
    break


def countdown(num):
  if num <= 0:
    print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
  for i in range(num, 0, -1):
    print(i)

countdown(0)
countdown(10)


sen1, sen2 = input().split(', ')
if len(sen1) > len(sen2):
  print(sen1)
else:
  print(sen2)


def square(num):
  print('square(%d) => %d' %(num, num**2))

numList = map(int, input().split(', '))
for i in numList:
  square(i)


def factorial(num):
  if num == 1:
    return 1
  output = num * factorial(num-1)
  return output

print(factorial(int(input())))


def findNum(numList, num):
  print('%d =>' %num, str(True if num in numList else False))

numList = [2, 4, 6, 8, 10]
print(numList)
findNum(numList, 5)
findNum(numList, 10)


def noDup(numList):
  result = list(dict.fromkeys(numList))
  return result

numList = [1, 2, 3, 4, 3, 2, 1]
print(numList)
print(noDup(numList))


a, b = map(int, input().split())
if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
  print('A')
else:
  print('B')


string = input()
for i in string:
  print(ord(i)-64, end=' ')


a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)


P, K = map(int, input().split())
print(P-K+1)


num = int(input())
n = 1
i = 1

while (i <= num+1):
  print(n, end = ' ')
  n *= 2
  i += 1


num = int(input())
print((num*(num+1)//2))


print('''#++++
+#+++
++#++
+++#+
++++#''')


T = int(input())

for i in range(T):
  a, b = map(int, input().split())
  print('#%d %d %d' %(i+1, a//b, a%b))


num = int(input())
for i in range(1, num+1):
  if num % i == 0:
    print(i, end = ' ')


a = int(input())
print(1*a + 11*a + 111*a + 1111*a)


T = int(input())
for i in range(T):
  numList = list(map(int, input().split()))
  result = 0
  for j in numList:
    if j % 2 == 1:
      result += j
  print('#%d %d' %(i+1, result))


T = int(input())
for i in range(T):
  numList = list(map(int, input().split()))
  print('#%d %d' %(i+1, round(sum(numList)/10)))


N = int(input())
numList = list(map(int, input().split()))
numList.sort()
print(numList[N//2])


T = int(input())
for i in range(T):
  a, b = map(int, input().split())
  result = ''
  if a < b:
    result = '<'
  elif a > b:
    result = '>'
  else:
    result = '='
  print('#%d' %(i+1), result)


T = int(input())
for i in range(T):
  numList = list(map(int, input().split()))
  numList.sort()
  print('#%d' %(i+1), numList[9])


N = int(input())
result = 0
while N > 10:
  result += (N % 10)
  N = N // 10
print(result+N)


def isCorrectDate(month, num):
  month, num = int(month), int(num)
  if month in (4, 6, 9, 11) and num <= 30:
    return True
  elif month == 2 and num <= 28:
    return True
  elif month in (1, 3, 5, 7, 8, 10, 12) and num <= 31:
    return True
  else:
    return False


def isCorrectMonth(num):
  num = int(num)
  if 1 <= num <= 12:
    return True
  else:
    return False


T = int(input())
for i in range(T):
  num = input()
  year = num[0:4]
  month = num[4:6]
  date = num[6:]
  if not isCorrectMonth(month) or not isCorrectDate(month, date):
    print("#%d -1" %(i+1))
    continue
  print('#%d '%(i+1) +  year + '/' + month + '/' + date)


num = int(input())
for i in range(num, -1, -1):
  print(i, end = ' ')


n = int(input())
print('#'*n)


string = input()
print(string.upper())


kg = float(input())
print('%0.2f kg =>  %0.2f lb' %(kg, kg*2.2046))


n = int(input())
for i in range(1, n+1):
  if n % i == 0:
    print('%d(은)는 %d의 약수입니다.' %(i, n))


n = int(input())
result = (n - 32) * (5/9)
print(result)


print("%0.2f" %((20/300)*100))


def palindrome(string):
  print(string[::-1])
  return string[::-1]


string = input()
reversedString = palindrome(string)
if string == reversedString:
  print('입력하신 단어는 회문(Palindrome)입니다.')
else:
  print('입력하신 단어는 회문(Palindrome)이 아닙니다.')


string = input()
if string.isalpha():
  if string.islower():
    print('%c(ASCII: %d) => %c(ASCII: %d)' %(string, ord(string), string.upper(), ord(string.upper())))
  else:
    print('%c(ASCII: %d) => %c(ASCII: %d)' %(string, ord(string), string.lower(), ord(string.lower())))
else:
  print('%c(ASCII: %d)'%(string, ord(string)))


for i in range(1, 101):
  print(i)


first = True

for num in range(100, 301):
  if ((num // 100) % 2 == 0) and (((num%100) // 10) % 2 == 0) and ((num % 10) % 2 == 0):
    if first:
      first = False
    else:
      print(',', end='')
    print(num, end = '')


first = True

for num in range(1, 201):
  if num % 7 == 0 and num % 5 != 0:
    if first:
      first = False
    else:
      print(',', end='')
    print(num, end = '')

for num in range(2, 101, 2):
  print(num, end = ' ')


name = input()
age = int(input())

# 100세가 되는 해를 계산합니다.
year_100 = 2019 + (100 - age)

print(f"{name}(은)는 {year_100}년에 100세가 될 것입니다.")


def rockscissors(man1, man2):
  rockscissorsList = ['가위', '바위', '보']
  man1Index = rockscissorsList.index(man1)
  man2Index = rockscissorsList.index(man2)
  if man1Index == man2Index:
    print('비겼습니다!')
  elif man1Index - man2Index == 1:
    print(man1+'가 이겼습니다!')
  elif man2Index - man2Index == 1:
    print(man2+'가 이겼습니다!')
  elif man1Index == 0 and man2Index == 2:
    print(man1+'가 이겼습니다!')
  else:
    print(man2+'가 이겼습니다!')

man1Name = input()
man2Name = input()
man1 = input()
man2 = input()
rockscissors(man1, man2)


print(1, end = '')

for i in range(3, 100, 2):
  print(', ', end = '')
  print(i, end = '')


result = 0
for num in range(3, 100, 3):
  result += num
print('1부터 100사이의 숫자 중 3의 배수의 총합: %d' %result)


bloodTypeList = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
bloodTypeDict = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}
for i in bloodTypeList:
  bloodTypeDict[i] += 1
print(bloodTypeDict)


num = int(input())
print(bin(num)[2:])


studentList = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0
while len(studentList) > 0:
  score = studentList.pop()
  if score >= 80:
    result += score

print(result)


i = 0

while i < 4:
  print(' '*i + '*'*(7-i*2)+' '*i)
  i += 1


i = 5
while i > 0:
  print('*'*i)
  i -= 1


num = int(input())
if num == 1:
  print('소수가 아닙니다.')
else:
  for i in range(2, num):
    if num % i == 0:
      print('소수가 아닙니다.')
      break
  else:
    print('소수입니다.')


string = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
total = list(map(lambda x: ord('E') - ord(x), string))
print(sum(total))


class Student():
  def __init__(self, korean, english, math):
    self.korean = korean
    self.english = english
    self.math = math

  def totalScore(self):
    return self.korean + self.english + self.math

student = Student(89, 90, 100);

print('국어, 영어, 수학의 총점:', student.totalScore())


num = int(input())
numList = [1, 1]
for i in range(2, num):
  numList.append(numList[i-1] + numList[i-2])
print(numList)


scoreList = [(90, 80), (85, 75), (90, 100)]
num = 0
for i in scoreList:
  print('%d번 학생의 총점은 %d점이고, 평균은 %0.1f입니다.' %(num+1, i[0]+i[1], (i[0]+i[1])/2))
  num += 1


alphaDict = {'a': 0, 'b': 1, 'c': 2, 'd':3, 'e': 4, 'f': 5}
for key, item in alphaDict.items():
  print('%c: %d'%(key, item))


string = list(input().split(','))
result = 1
for num in string:
  try:
    result *= int(num)
  except:
    print('에러발생')
    break
else:
  print(result)


resultList = []
for num in range(2, 10):
  result = []
  for num2 in range(1, 10):
    num3 = num * num2
    if num3 % 3 != 0 and num3 % 7 != 0:
      result.append(num3)
  resultList.append(result)
print(resultList)


numList = [i for i in range(1, 11)]

resultList = list(map(lambda x:x**2, filter(lambda x: True if x % 2 == 0 else False, numList)))
print(resultList)


string = int(input())
print('ASCII %d => %c' %(string, chr(string)))


numList = [num for num in range(1, 11)]
result = list(filter(lambda x: True if x % 2 == 0 else False, numList))
print(result)


def getMax(numList):
  numList = list(map(int, string.split(',')))
  return max(numList)

string = '3, 5, 4, 1, 8, 10, 2'
numList = list(map(int, string.split(',')))
print('max('+string+') => '+str(getMax(numList)))


numList = [num for num in range(1, 11)]
resultList = list(map(lambda x: x**2, numList))
print(resultList)


class Korean():
  def __init__(self, nationality):
    self.nationality = nationality

  def printNationality(self):
    print(self.nationality)
    print(self.nationality)

korean = Korean('대한민국')
korean.printNationality()


class Student():
  def __init__(self, name):
    self.name = name

  def printName(self):
    print('이름: ' + self.name)

class GraduateStudent():
  def __init__(self, name, major):
    self.student = Student(name)
    self.major = major

  def printNameAndMajor(self):
    print('이름: ' + self.student.name + ', 전공: ' + self.major)

student = Student('홍길동')
graduateStudent = GraduateStudent('이순신', '컴퓨터')
student.printName()
graduateStudent.printNameAndMajor()


class Student():
  def __init__(self, name):
    self.name = name

  def printName(self):
    print('이름: ' + self.name)

class GraduateStudent(Student):
  def __init__(self, name, major):
    super().__init__(name)
    self.major = major

  def printNameAndMajor(self):
    print('이름: ' + self.name + ', 전공: ' + self.major)

student = Student('홍길동')
graduateStudent = GraduateStudent('이순신', '컴퓨터')
student.printName()
graduateStudent.printNameAndMajor()


string = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
string = string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
print(string)


numList = list()
for i in range(5):
  num = int(input())
  numList.append(num)
print('입력된 값 '+str(numList)+'의 평균은 %0.1f입니다.'%(sum(numList)/len(numList)))


numList = [int(input()) for _ in range(5)]
print('입력된 값 '+str(numList)+'의 평균은 %0.1f입니다.'%(sum(numList)/len(numList)))


class Parent():
    def getGender(self):
        return 'Unknown'

class Male(Parent):
    def getGender(self):
        return 'Male'
class Female(Parent):
    def getGender(self):
        return 'Female'

male = Male()
female = Female()
print(male.getGender())
print(female.getGender())


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

circle = Circle(2)
print('원의 면적: %.2f' % (math.floor(circle.area() * 100) / 100))


num = int(input())
numList = [i for i in range(1, num+1) if num % i == 0 ]
print(numList)


num = int(input())
numList = [i for i in range(1, num+1) if num % i == 0]
print(numList)


numList = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
resultList = list(filter(lambda x: x % 2 == 0, numList))
print(resultList)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangle1 = Rectangle(10, 2)
print('사각형의 면적:', rectangle1.area())


class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

square = Square(3)
print('정사각형의 면적:', square.area())

def noDup(numList):
    resultList = []
    for n in numList:
        if n not in resultList:
            resultList.append(n)
    return resultList

numList = [12,24,35,24,88,120,155,88,120,155]
print(noDup(numList))


numList = [1, 1]
resultList = [numList.append(numList[i-1]+numList[i]) for i in range(1, 9)]
print(numList)


string = input()
result = 0
for num in string:
    result += int(num)
print(result)


numList = [5, 6, 77, 45, 22, 12, 24]
resultList = [num for num in numList if num % 2 != 0]
print(resultList)

resultList = [num**2 for num in range(1, 21) if num % 3 != 0 or num % 5 != 0]
print(resultList)


dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'),
           ('바','빟'), ('사','싷'), ('아','잏'), ('자','짛'),
           ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀',
             '들다', '싶다', '수출', '계시다', '다', '뒤', '듣다', '함께', '아이',
             '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개',
             '정도', '옳다', '놀이', '뜨겁다']

result = [
    [w for w in inputWord if ord(r[0]) <= ord(w[0]) <= ord(r[1])]
    for r in dicBase
]

print(result)


string = input()
backString = string[::-1]
print(backString)
if string == backString:
    print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    print('입력하신 단어는 회문(Palindrome)이 아닙니다.')


numberDict = {
    '홍길동': '010-1111-1111',
    '이순신': '010-1111-2222',
    '강강찬': '010-1111-3333'
}
name = input('''아래 학생들의 전화번호를 조회할 수 있습니다.
홍길동
이순신
강감찬
전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.''')
print(name+'의 전화번호는 '+numberDict[name]+'입니다.')


numList = list(map(int, input().split(',')))
numTuple = tuple(numList)
print(numList)
print(numTuple)


import math

radiusList = list(map(int, input().split(',')))
circumferenceList = [round(num*2*math.pi, 2) for num in radiusList]
print(*circumferenceList, sep=', ')


row, col = map(int, input().split(','))
resultList = [[i*j for j in range(col)] for i in range(row)]
print(resultList)


numList1 = [1,3,6,78,35,55]
numList2 = [12,24,35,24,88,120,155]
resultList = [num for num in numList1 if num in numList2]
print(resultList)


string = input()
result = string[0::2]
print(result)


string = input().split(',')
string = [w.strip() for w in string]
string.sort()
print(', '.join(string))


numList = list(map(int, input().split(',')))
numList = [num for num in numList if num % 2 != 0]
print(', '.join(map(str, numList)))


resultList = [[[0 for _ in range(4)] for j in range(3)] for i in range(2)]
print(resultList)


numList = [12, 24, 35, 70, 88, 120, 155]
resultList = [numList[i] for i in range(len(numList)) if i not in (0, 4, 5)]
print(resultList)


numList = [12, 24, 35, 70, 88, 120, 155]
resultList = numList[1::2]
print(resultList)


numTuple = (1,2,3,4,5,6,7,8,9,10)
numTuple1 = numTuple[0:len(numTuple)//2]
numTuple2 = numTuple[len(numTuple)//2:]
print(numTuple1)
print(numTuple2)


productDict = { "TV": 2000000, "냉장고": 1500000, "책상": 350000, "노트북": 1200000, "가스레인지": 200000, "세탁기": 1000000}
sortedProductDict = sorted(productDict.items(), key=lambda x: x[1], reverse=True)
for key, value in sortedProductDict:
    print(key + ': ' + str(value))


stringList = input().split()
stringList = stringList[::-1]
print(*stringList)


from collections import defaultdict
string = input()
stringDict = defaultdict(int)
for char in string:
    stringDict[char] += 1
for key, value in stringDict.items():
    print(key + ',' + str(value))
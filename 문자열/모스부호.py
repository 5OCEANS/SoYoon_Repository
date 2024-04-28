import sys

N = int(sys.stdin.readline())

morseList = sys.stdin.readline().strip().split()

string = ''

for i in morseList:
  if len(i) == 6:
    if i == '--..--':
      string += ','
    elif i == '.-.-.-':
      string += '.'
    elif i == '..--..':
      string += '?'
    elif i == '---...':
      string += ':'
    elif i == '-....-':
      string += '-'
    elif i == '.--.-.':
      string += '@'

  elif len(i) == 5:
    if i == '.----':
      string += '1'
    elif i == '..---':
      string += '2'
    elif i == '...--':
      string += '3'
    elif i == '....-':
      string += '4'
    elif i == '.....':
      string += '5'
    elif i == '-....':
      string += '6'
    elif i == '--...':
      string += '7'
    elif i == '---..':
      string += '8'
    elif i == '----.':
      string += '9'
    elif i == '-----':
      string += '0'
  
  else:
    if i == '.-':
      string += 'A'
    elif i == '-...':
      string += 'B'
    elif i == '-.-.':
      string += 'C'
    elif i == '-..':
      string += 'D'
    elif i == '.':
      string += 'E'
    elif i == '..-.':
      string += 'F'
    elif i == '--.':
      string += 'G'
    elif i == '....':
      string += 'H'
    elif i == '..':
      string += 'I'
    elif i == '.---':
      string += 'J'
    elif i == '-.-':
      string += 'K'
    elif i == '.-..':
      string += 'L'
    elif i == '--':
      string += 'M'
    elif i == '-.':
      string += 'N'
    elif i == '---':
      string += 'O'
    elif i == '.--.':
      string += 'P'
    elif i == '--.-':
      string += 'Q'
    elif i == '.-.':
      string += 'R'
    elif i == '...':
      string += 'S'
    elif i == '-':
      string += 'T'
    elif i == '..-':
      string += 'U'
    elif i == '...-':
      string += 'V'
    elif i == '.--':
      string += 'W'
    elif i == '-..-':
      string += 'X'
    elif i == '-.--':
      string += 'Y'
    elif i == '--..':
      string += 'Z'

print(string)
import sys

morse_dict = {
  'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
  'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
  'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
  'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
  'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
  'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
  'Y': '-.--',  'Z': '--..',  '_': '..--', ',': '.-.-',
  '.': '---.',  '?': '----'
}

reverse_morse = {v: k for k, v in morse_dict.items()}

n = int(sys.stdin.readline())
for i in range(1, n + 1):
  line = sys.stdin.readline().strip()
  morse = ''
  lengths = ''

  for ch in line:
    code = morse_dict[ch]
    morse += code
    lengths += str(len(code))

  lengths = lengths[::-1]

  decoded = []
  idx = 0
  for l in lengths:
    l = int(l)
    segment = morse[idx:idx + l]
    decoded.append(reverse_morse[segment])
    idx += l

  print(f"{i}: {''.join(decoded)}")
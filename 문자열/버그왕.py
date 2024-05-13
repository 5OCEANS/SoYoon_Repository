import sys
import re

code = sys.stdin.readlines() # 여러 줄을 입력받을 수 있는 함수 콘솔창에서는 다 입력하고 ctrl + z를 눌러주면 입력을 그만 받을 수 있음. -> 

for i in code:

  while True:
    result = re.sub('BUG', '', i) # sub(패턴, 교체할 문자열, 최대 교체 수, 플래그) - 문자열에 맞는 패턴을 2번째 인자로 교체 split의 최대 split 수와 동일하게 최대 교체 수를 지정하면 문자열에 맞는 패턴을 교체할 문자열로 교체하고 그 수가 도달하면 더이상 교체하지 않음.

    if 'BUG' in result:
      i = result 
    else:
      print(result, end = '')
      break

# sub() 함수 예시

import re

print(re.sub('a', 'z', 'ab'))       # zb
print(re.sub('a', 'zxc', 'ab'))     # zxcb
print(re.sub('a', 'z', 'aaaab'))     # zzzzb
print(re.sub('a', 'z', 'aaaab', 1))  # zaaab
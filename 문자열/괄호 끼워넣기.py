import sys

s = sys.stdin.readline().rstrip()
stack = []
ret = 0
for c in s:
	if c == '(': # 여는 괄호가 나오면
		stack.append(c) # stack에 넣어 둠
	else: # 닫는 괄호가 나오면
		if stack: # 여는 괄호가 stack에 있을 때는 짝이 맞기 때문에
			stack.pop() # stack에서 pop시킴
		else: # 여는 괄호가 없으면 짝이 맞지 않기 때문에
			ret += 1 # +1

ret += len(stack)  # 마지막에 짝이 맞지 않아 stack에 남아있는 결과 + ret
print(ret)
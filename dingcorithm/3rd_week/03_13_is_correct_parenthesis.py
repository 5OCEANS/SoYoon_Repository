def is_correct_parenthesis(string):
    parenthesis_stack = []

    for char in string:
        if char == ')':
            if len(parenthesis_stack) == 0:
                return False
            if parenthesis_stack[-1] == '(':
                parenthesis_stack.pop()

        else:
            parenthesis_stack.append(char)

    if len(parenthesis_stack) == 0:
        return True
    return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
def is_correct_parenthesis(string):
    index = len(string)
    stacks = []

    for i in range(index) :
        if string[i] == '(' :
            stacks.append(i)
        else :
            if len(stacks) == 0 :
                return False
            stacks.pop()

    if len(stacks) != 0 :
        return False
    else :
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
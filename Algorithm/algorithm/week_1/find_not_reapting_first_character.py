def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    curChar = '_'
    for char in list(string):
        if not char.isalpha():
            continue

        if curChar == '_' :
            curChar = char
        else :
            if char == curChar :
                curChar = '_'  
    return curChar


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))
print("정답 = k 현재 풀이 값 =", result("a*aa*a&&aaaak"))
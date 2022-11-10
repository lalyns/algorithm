input = "토마토"


def is_palindrome(string):
    # strLen = len(string)

    # for i in range(strLen) :
    #     if string[i] != string[strLen - 1] :
    #         return False
    #     else :
    #         return True
    if len(string) <= 1 :
        return True

    if string[0] != string[-1] :
        return False
    else :
        return is_palindrome(string[1:-1])
    
        

print(is_palindrome(input))
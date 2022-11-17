def solution(x):
    a = sum(int(c) for c in str(x)) 
    answer = x % a == 0
    return answer

print(solution(12345))
def solution(n):
    answer = 0
    m = str(n)
    
    for i in range(len(m)) :
        answer += int(m[i])
    
    return answer
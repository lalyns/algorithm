def solution(order):
    order_str = str(order)
    
    answer = 0
    
    for i in range(len(order_str)):
        if order_str[i] == '3' or order_str[i] == '6' or order_str[i] == '9':
            answer += 1
        
    
    return answer
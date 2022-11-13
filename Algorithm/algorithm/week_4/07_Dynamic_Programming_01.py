input = 20


def fibo_recursion(n):
    # start = 2 
    # fibo = [1, 1]

    # if n <= 2 :
    #     if n <= 0 :
    #         return
    #     return fibo(n-1)

    # while start < n:
    #     newfibo = fibo[start-1] + fibo[start-2]
    #     fibo.append(newfibo)
    #     start += 1
    #     return fibo[n-1]
    # 구현해보세요!

    if n == 1 or n == 2:
        return 1
    
    return fibo_recursion(n-1) + fibo_recursion(n-2)



print(fibo_recursion(input))  # 6765
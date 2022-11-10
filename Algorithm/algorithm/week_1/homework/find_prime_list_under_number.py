import math

input = 17785

def find_prime_list_under_number(number):
    array = [True for i in range(number + 1)]
    array[0] = False
    array[1] = False
    result = []

    for i in range(2, int(math.sqrt(number) + 1)) :
        if array[i] == True:
            j=2
            while i*j <= number:
                array[ i * j ] = False
                j += 1
    
    for i in range(len(array)) :
        if array[i] :
            result.append(i)

    return result


result = find_prime_list_under_number(input)
print(result)
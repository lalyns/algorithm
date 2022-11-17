def merge_sort(array):
    if len(array) <= 1 :
        return array

    mid = len(array) // 2

    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)

def merge(array1, array2) :
    result = []

    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2) :
        if array1[array1_index] > array2[array2_index] :
            result.append(array1[array1_index])
            array1_index += 1
        else :
            result.append(array2[array2_index])
            array2_index += 1
        
    if array1_index == len(array1) :
        while array2_index < len(array2) :
            result.append(array2[array2_index])
            array2_index += 1
    
    if array2_index == len(array2) :
        while array1_index < len(array1) :
            result.append(array1[array1_index])
            array1_index += 1

    return result

def solution(n):
    m = str(n)
    array = [0] * len(m)
    
    for i in range(len(m)):
        array[i] = int(m[i])

    array = merge_sort(array)

    print(array)

    answer = ''

    for i in array:
        answer += str(i)

    return answer

solution(118372)
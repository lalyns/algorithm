numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0 


def get_how_to_target_numbers(array, target, cur_index, cur_sum):
    if cur_index == len(array):  
        if cur_sum == target:
            global result_count
            result_count += 1  
        return
    get_how_to_target_numbers(array, target, cur_index + 1, cur_sum + array[cur_index])
    get_how_to_target_numbers(array, target, cur_index + 1, cur_sum - array[cur_index])


get_how_to_target_numbers(numbers, target_number, 0, 0)
print(result_count)  
input = "011010101011010101010101010101010101010101010101010101011111000101010101010011011000011101100110101010110101010101010101010101010101010101010101010111110001010101010100110110000111011001101010101101010101010101010101010101010101010101010101111100010101010101001101100001110110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    str_list = list(string)
    curStr = ''
    divIndex = []

    for index in range(len(str_list)) :
        if curStr == str_list[index] :
            continue
        else :
            curStr = str_list[index]
            divIndex.append(index)
    
    return len(divIndex) // 2;

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
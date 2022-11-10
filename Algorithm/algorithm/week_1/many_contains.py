input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    str_list = list(string)
    alphabet_occurrence_array = [0] * 26
    for char in str_list:
        if not char.isalpha() :
            continue
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1
    
    max_occurrence = alphabet_occurrence_array[0]
    max_index = 0 ;
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]
        if alphabet_occurence > max_occurrence:
            max_occurrence = alphabet_occurence
            max_index = index
    
    return chr(max_index + 97)

result = find_max_occurred_alphabet(input)
print(result)
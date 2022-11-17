input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []

    for split in range(1, n//2 + 1) :
        compressed = ""
        splited = [ 
            string[i:i+split] for i in range(0, n, split)
        ]
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count += 1
            else :
                if count > 1:
                    compressed += (str(count) + prev)
                else :
                    compressed += prev
                count = 1
        if count > 1:
            compressed += (str(count) + splited[-1])
        else :
            compressed += splited[-1]
        compression_length_array.append(compressed)

    return len(min(compression_length_array))


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
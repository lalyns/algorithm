def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    length = len(genre_array)
    genre_total_played = {}
    play_array_dict = {}

    for i in range(length) :
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_total_played :
            genre_total_played[genre] = play
            play_array_dict[genre] = [[i, play]]
        else :
            genre_total_played[genre] += play
            play_array_dict[genre].append([i, play])

    sorted_genre_arr = sorted(genre_total_played.items(), key=lambda item: item[1], reverse=True)
    result = [] 

    for gerne, _value in sorted_genre_arr:
        index_play = play_array_dict[gerne]
        sorted_play = sorted(index_play, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_play)) :
            if i > 1 :
                break
            result.append(sorted_play[i][0])

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
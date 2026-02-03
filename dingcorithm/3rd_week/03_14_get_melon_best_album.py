def get_melon_best_album(genre_array, play_array):
    # 버전 1
    answer = []
    music_dict = dict()
    for idx in range(len(genre_array)):
        if genre_array[idx] not in music_dict.keys():
            music_dict[genre_array[idx]] = [[idx, play_array[idx]]]
        else:
            music_dict[genre_array[idx]].append([idx, play_array[idx]])

    sorted_by_play_music_dict = dict(sorted(music_dict.items(), key= lambda x:(sum(play for _, play in x[1])), reverse=True))
    print(sorted_by_play_music_dict)
    for key, musics in sorted_by_play_music_dict.items():
        sorted_musics = sorted(musics, key=lambda x:(-x[1], x[0]))
        for idx, _ in sorted_musics[:2]:
            answer.append(idx)

    # 버전 2
    n = len(genre_array)
    genre_total_play_dict = dict()
    genre_index_play_array_dict = dict()

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

        sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse=True)

        answer = []

        for genre, total_play in sorted_genre_play_array:
            sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item:item[1], reverse=True)

            genre_song_count = 0
            for index, play in sorted_genre_index_play_array:
                if genre_song_count >= 2:
                    break

                answer.append(index)
                genre_song_count += 1

    return answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
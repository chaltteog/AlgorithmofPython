# def solution(genres, plays):
#     answer = []
#     album = {}
#     lank = []
    
#     for i in range(len(genres)):
#         if not genres[i] in album:
#             album[genres[i]] = {}
            
#         album[genres[i]][i] = plays[i]
        
#     print(f"album => {album}")
#     for genres_type in album.keys():
#         genres_dict = album[genres_type]
#         total = 0
#         songs = []
#         max_num = -1
#         min_num = -1

#         for key, value in genres_dict.items():
#             print(f"songs => {songs}")
#             print(f"{key} / {value}")
#             total += value
            
#             if max_num < value:
#                 songs.insert(0, key)
#                 max_num = value
#                 continue

#             if min_num < value:
#                 songs.insert(1, key)
#                 min_num = value
#                 continue

#         print(songs)        
#         lank.append([total, songs])

#     lank.sort(key = lambda x:-x[0])

#     for genres_list in lank:
#         answer += genres_list[1][:2]

#     return answer

def solution(genres, plays):
    answer = []
    total = {}
    songs = {}
    
    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        songs[genres[i]] = songs.get(genres[i], []) + [(plays[i], i)]
    
    total = sorted(total.items(), key = lambda x: -x[1])
    
    for genre, cnt in total:
        songs[genre] = sorted(songs[genre], key = lambda x: (-x[0], x[1]))

        for (play, idx) in songs[genre][:2]:
            answer.append(idx)
    
    return answer

print(solution(["classic", "classic", "classic", "pop"], [0, 1, 2, 0]))
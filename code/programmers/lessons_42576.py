participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

'''
첫번째 문제 풀이 Hash를 미사용함
- Hash의 관한 알고리즘이지만 Hash를 사용하지않고 풀어 버림
'''
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
    
#     return participant[i+1]

'''
두번째 문제 풀이 Hash를 사용함
'''
def solution(participant, completion):
    dic = {}
    num = 0
    
    for player in participant:
        dic[hash(player)] = player
        num += hash(player)

    for complet in completion:
        num -= hash(complet)

    return dic[num]

print(solution(participant,completion))
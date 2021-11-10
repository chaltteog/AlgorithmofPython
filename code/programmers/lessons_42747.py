def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    print(citations)

    for i in range(len(citations)):
        pos = i + 1
        if citations[i] >= pos:
            print(f'no=>{pos}/value=>{citations[i]}')
            answer = pos
    
    return answer

print(solution([3, 0, 6, 1, 5]))
# print(solution([0, 0, 0, 0, 0])) #answer 0
# print(solution([0, 0, 0, 0, 1])) #answer 1
print(solution([9, 9, 9, 12])) #answer 4
# print(solution([9, 7, 6, 2, 1])) #answer 3
# print(solution([10, 8, 5, 4, 3])) #answer 4
# print(solution([25, 8, 5, 3, 3])) #answer 3
print(solution([1, 1, 5, 7, 6])) #answer 3
# print(solution([0])) #answer 0
# print(solution([0, 0])) #answer 0

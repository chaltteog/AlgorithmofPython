def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1

        temp_arr = array[i:j]
        temp_arr.sort()

        answer.append(temp_arr[k])

    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
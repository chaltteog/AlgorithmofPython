# def solution(numbers):
#     str_numbers = list(map(str, numbers))
#     str_numbers.sort(reverse=True)

#     return ''.join(str_numbers)

# def solution(numbers):
#     str_numbers = list(map(str, numbers))
#     str_numbers.sort(key= lambda n: n*3, reverse=True)

#     return ''.join(str_numbers)

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key= lambda n: n*3, reverse=True)

    return str(int(''.join(str_numbers)))

print(solution([6, 10, 2]))

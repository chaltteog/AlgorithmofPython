a = ["119", "97674223", "12590", "125"]

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        num = phone_book[i]
        phone_len = len(num)

        if num == phone_book[i+1][:phone_len]:
            return False

    return True

# def solution(phone_book):
#     phone_book.sort()

#     for i in range(len(phone_book) - 1):
#         num = phone_book[i]
        
#         if phone_book[i+1].startswith(num):
#             return False

#     return True

print(solution(a))
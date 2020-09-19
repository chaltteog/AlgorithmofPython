'''
프로그램명 : 2581.py
작성자 : 권혁진
작성일 : 2020-09-19
설명 : 소수
참조 : https://www.acmicpc.net/problem/2581
'''

def is_prime_number(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num):
        if num % i == 0:
            return False

    return True

min_num = int(input())
max_num = int(input())

if max_num < 2:
    print(-1)
    exit()

num_list = list(range(min_num, max_num + 1))
out = list(range(min_num, max_num + 1))

total = 0

for num in num_list:
    if is_prime_number(num):        
        total += num
        continue

    out.remove(num)

if total == 0:
    print(-1)
else:
    print(total)
    print(out[0])

'''
프로그램명 : 1978.py
작성자 : 권혁진
작성일 : 2020-09-18
설명 : 소수 찾기
참조 : https://www.acmicpc.net/problem/1978
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

count = int(input())
num_list = list(map(int, input().split()))
prime_cnt = 0

for num in num_list:          
    if is_prime_number(num):
        prime_cnt += 1

print(prime_cnt)
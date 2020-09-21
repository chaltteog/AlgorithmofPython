'''
프로그램명 : 1929.py
작성자 : 권혁진
작성일 : 2020-09-21
설명 : 소수 구하기
참조 : https://www.acmicpc.net/problem/1929
'''
import math

def is_prime_number(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    n = int(math.sqrt(num))
    for i in range(3, n + 1):
        if num % i == 0:
            return False

    return True

min_num, max_num = map(int, input().split())

for num in range(min_num, max_num + 1):          
    if is_prime_number(num):
        print(num)

'''
프로그램명 : 10870.py
작성자 : 권혁진
작성일 : 2020-09-02
설명 : 피보나치 수 5
참조 : https://www.acmicpc.net/problem/10870
'''

def get_fibonacci_numbers(num):
    if num == 0:
        return 0

    if num == 1:
        return 1
        
    return get_fibonacci_numbers(num - 1) + get_fibonacci_numbers(num - 2)


print(get_fibonacci_numbers(int(input())))

'''
프로그램명 : 10872.py
작성자 : 권혁진
작성일 : 2020-09-02
설명 : 팩토리얼
참조 : https://www.acmicpc.net/problem/10872
'''

def get_factorial(num):
    if num <= 1:
        return 1

    return num * get_factorial(num - 1)


print(get_factorial(int(input())))

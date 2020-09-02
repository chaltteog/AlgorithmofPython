'''
프로그램명 : 2908.py
작성자 : 권혁진
작성일 : 2020-09-01
설명 : 상수
참조 : https://www.acmicpc.net/problem/2908
'''

def diff_num(num1, num2):
    cnt = num1 - num2

    if cnt == 0:
        return num1
    
    if cnt > 0:
        return num1

    if cnt < 0:
        return num2


a, b = map(str, input().split())

a = int(''.join(reversed(a)))
b = int(''.join(reversed(b)))

print(diff_num(a, b))
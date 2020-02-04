'''
프로그램명 : 10952.py
작성자 : 권혁진
작성일 : 2020-02-04
설명 : A+B - 5
'''

a, b = map(int, input().split())

while (a != 0) and (b != 0):
    print('%d' %(a+b))
    a, b = map(int, input().split())
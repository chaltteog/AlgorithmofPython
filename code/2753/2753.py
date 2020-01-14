'''
프로그램명 : 2753.py
작성자 : 권혁진
작성일 : 2020-01-14
설명 : 윤년
'''

year = int(input())

if year % 4:
    print('0')
    exit()

if not year % 400:
    print('1')
    exit()

if year % 100:
    print('1')
    exit()
else:
    print('0')
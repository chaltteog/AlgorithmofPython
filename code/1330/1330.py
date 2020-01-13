'''
프로그램명 : 1330.py
작성자 : 권혁진
작성일 : 2020-01-07
설명 : 두 수 비교
'''

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
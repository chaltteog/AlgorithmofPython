'''
프로그램명 : 9498.py
작성자 : 권혁진
작성일 : 2020-01-13
설명 : 시험 성적
'''

grade = int(input())

if grade > 89:
    print('A')
elif grade > 79:
    print('B')
elif grade > 69:
    print('C')
elif grade > 59:
    print('D')
else:
    print('F')
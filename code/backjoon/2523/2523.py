'''
프로그램명 : 2523.py
작성자 : 권혁진
작성일 : 2020-07-07
설명 : 별 찍기 - 13
'''
cnt = int(input())
star = ''

for i in range(0, cnt):
    for j in range(0, i + 1):
        star += '*'
    print(star)
    star = ''

for i in range(cnt - 1, 0, -1):
    for j in range(0, i):
        star += '*'
    print(star)
    star = ''

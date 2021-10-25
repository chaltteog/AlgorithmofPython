'''
프로그램명 : 2884.py
작성자 : 권혁진
작성일 : 2020-01-14
설명 : 알람 시계
'''

h, m = map(int, input().split())

m -= 45

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h = 23

print(h, ' ', m)    
'''
프로그램명 : 10817.py
작성자 : 권혁진
작성일 : 2020-01-15
설명 : 세 수
'''

a, b, c = map(int, input().split())
ret = 0, 0, 0

if a > b:
    if b > c:
        ret = b
    else:
        if a > c:
            ret = c
        else:
            ret = a
else:
    if a > c:
        ret = a
    else:
        if b > c:
            ret = c
        else:
            ret = b

print(ret)
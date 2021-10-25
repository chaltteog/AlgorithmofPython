'''
프로그램명 : 14681.py
작성자 : 권혁진
작성일 : 2020-05-02
설명 : 사분면 고르기
'''
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if ((x > 0) and (y > 0)):
    print(1)
elif ((x < 0) and (y > 0)):
    print(2)
elif ((x < 0) and (y < 0)):
    print(3)
elif ((x > 0) and (y < 0)):
    print(4)        
'''
프로그램명 : 10950.py
작성자 : 권혁진
작성일 : 2020-01-18
설명 : A+B - 3
'''

cnt = int(input())

for i in range(0, cnt):
    a, b = map(int, input().split())
    print("%d" %(a+b))
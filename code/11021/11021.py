'''
프로그램명 : 11021.py
작성자 : 권혁진
작성일 : 2020-01-30
설명 : A+B - 7
'''
cnt = int(input()) + 1

for i in range(1, cnt):    
    a, b = map(int, input().split())
    print("Case #%d: %d" %(i, a+b))
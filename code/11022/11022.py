'''
프로그램명 : 11022.py
작성자 : 권혁진
작성일 : 2020-02-01
설명 : A+B - 8
'''
cnt = int(input()) + 1

for i in range(1, cnt):    
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i, a, b, a+b))
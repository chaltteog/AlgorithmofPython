'''
프로그램명 : 2438.py
작성자 : 권혁진
작성일 : 2020-02-01
설명 : 별 찍기 - 1
'''
cnt = int(input()) + 1
star = ""

for i in range(1, cnt):    
    star += "*"
    print("%s" %(star))
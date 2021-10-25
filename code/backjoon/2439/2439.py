'''
프로그램명 : 2439.py
작성자 : 권혁진
작성일 : 2020-02-01
설명 : 별 찍기 - 2
'''
cnt = int(input())
star = space = ""

space = space.ljust(cnt, " ")

for i in range(0, cnt):    
    star += "*"
    print("%s%s" %(space[1:cnt-i], star))
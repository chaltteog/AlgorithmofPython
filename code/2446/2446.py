'''
프로그램명 : 2446.py
작성자 : 권혁진
작성일 : 2020-08-20
설명 : 별 찍기 - 9
'''


def MakeStars(cnt, max):
    space = ""
    outStr = ""
    i = 1

    spaceCnt = max - cnt
    cnt *= 2

    while i < spaceCnt:
        space += " "
        i += 1

    while cnt >= 0:
        outStr += "*"
        cnt -= 1

    print(space + outStr)    
    return
    
num = int(input())

for i in range(num - 1, 0, -1):
    MakeStars(i, num)

for i in range(0, num):
    MakeStars(i, num)
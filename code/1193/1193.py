'''
프로그램명 : 1193.py
작성자 : 권혁진
작성일 : 2020-09-10
설명 : 분수찾기
참조 : https://www.acmicpc.net/problem/1193
'''

point = int(input())
stage = 1

while point > stage:
    point -= stage
    stage += 1

if stage % 2 == 0:
    x = point
    y = stage - point + 1
else:
    x = stage - point + 1
    y = point

print('{}/{}'.format(x, y))

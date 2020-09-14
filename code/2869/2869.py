'''
프로그램명 : 2869.py
작성자 : 권혁진
작성일 : 2020-09-14
설명 : 달팽이는 올라가고 싶다
'''

A, B, V = map(int, input().split())
K = (V - A) % (A - B)

cnt = (V - A) // (A - B)
if K == 0:
    print(cnt + 1)
    exit()

print(cnt + 2)
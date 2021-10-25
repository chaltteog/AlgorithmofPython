'''
프로그램명 : 5543.py
작성자 : 권혁진
작성일 : 2020-07-04
설명 : 상근날드
'''
import sys

buger, drink = [], [] 

for i in range(0, 3):
    buger.append(int(sys.stdin.readline()))

for i in range(0, 2):
    drink.append(int(sys.stdin.readline()))

buger.sort()
drink.sort()

print(buger[0] + drink[0] - 50)
'''
프로그램명 : 2577.py
작성자 : 권혁진
작성일 : 2020-07-04
설명 : 숫자의 개수
'''
import sys

num = 1

for i in range(0, 3):
    num *= int(sys.stdin.readline())

numList = list(map(int, list(str(num))))

for i in range(0, 10):
    print(numList.count(i))

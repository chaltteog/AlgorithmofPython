'''
프로그램명 : 3052.py
작성자 : 권혁진
작성일 : 2020-08-24
설명 : 나머지
참조 : https://www.acmicpc.net/problem/3052
'''
import sys

i = 0
numList = set()

while i < 10:
    numList.add(int(sys.stdin.readline()) % 42)
    i += 1

print(len(numList))

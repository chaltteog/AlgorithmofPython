'''
프로그램명 : 15552.py
작성자 : 권혁진
작성일 : 2020-01-21
설명 : 빠른 A+B
'''
import sys

cnt = int(sys.stdin.readline())

for i in range(0, cnt):
    a, b = map(int, sys.stdin.readline().split())
    print("%d" %(a+b))
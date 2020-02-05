'''
프로그램명 : 10951.py
작성자 : 권혁진
작성일 : 2020-02-05
설명 : A+B - 4
'''
import sys

for line in sys.stdin:    
    a, b = map(int, line.split())
    print(a+b)
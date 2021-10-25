'''
프로그램명 : 10430.py
작성자 : 권혁진
작성일 : 2020-01-07
설명 : 나머지
'''

A, B, C = map(int, input().split())

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
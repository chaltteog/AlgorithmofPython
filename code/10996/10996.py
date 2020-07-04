'''
프로그램명 : 10996.py
작성자 : 권혁진
작성일 : 2020-07-04
설명 : 별 찍기 - 21
'''
num = int(input())
div = num // 2
mod = num % 2

a, b = '', ''
aRange = div + mod
bRange = div

for i in range(0, aRange):
    a += '* '

for i in range(0, bRange):
    b += ' *'

for i in range(0, num):
    if b != '':
        print(a, b, sep='\n')
    else:
        print(a)
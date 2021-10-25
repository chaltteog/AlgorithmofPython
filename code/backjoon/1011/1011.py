'''
프로그램명 : 1011.py
작성자 : 권혁진
작성일 : 2020-09-12
설명 : Fly me to the Alpha Centauri
참조 : https://www.acmicpc.net/problem/1011
'''
from math import sqrt
case = int(input())

for _ in range(case):
    start, end = map(int, input().split())
    diff = end - start

    m = int(sqrt(diff))
    n = m + 1

    if m == 1:
        print(diff)
        continue

    if diff >= m * n + 1:
        print(m + n)
        continue

    if diff >= m ** 2 + 1:
        print(m * 2)
        continue

    print(m * 2 - 1)

'''
프로그램명 : 1712.py
작성자 : 권혁진
작성일 : 2020-09-07
설명 : 손익분기점
참조 : https://www.acmicpc.net/problem/1712
'''

fixed_cost, notebook_cost, sales_cost = map(int, input().split())
ret = 0

if sales_cost > notebook_cost:
    ret = fixed_cost // (sales_cost - notebook_cost) + 1
else:
    ret = -1

print(ret)

'''
프로그램명 : 1712.py
작성자 : 권혁진
작성일 : 2020-09-07
설명 : 손익분기점
참조 : https://www.acmicpc.net/problem/1712
'''

fixed_cost, notebook_cost, sales_cost = map(int, input().split())

profit = fixed_cost * -1
notebook_cnt = 0

while profit <= 0:
    notebook_cnt += 1

    profit = sales_cost * notebook_cnt    
    profit -= fixed_cost + notebook_cost * notebook_cnt    

print(notebook_cnt)

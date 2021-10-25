'''
프로그램명 : 2839.py
작성자 : 권혁진
작성일 : 2020-09-08
설명 : 설탕 배달
'''
import sys

suger_weight = int(input())
suger_bag_cnt = 0

while True:
    if suger_weight % 5 == 0:
        suger_bag_cnt += suger_weight // 5
        suger_weight = 0
        break

    suger_weight -= 3
    suger_bag_cnt += 1

    if suger_weight < 3:        
        break

if suger_weight != 0:
    suger_bag_cnt = -1

print(suger_bag_cnt)
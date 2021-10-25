'''
프로그램명 : 10039.py
작성자 : 권혁진
작성일 : 2020-07-06
설명 : 평균점수
'''
import sys

Total = 0

for i in range(0, 5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40

    Total += score

print(Total // 5)

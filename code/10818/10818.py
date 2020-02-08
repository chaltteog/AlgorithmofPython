'''
프로그램명 : 10818.py
작성자 : 권혁진
작성일 : 2020-02-08
설명 : 최소, 최대
'''
min = max = 0
cnt = int(input()) - 1

num = list(map(int, input().split()))
num.sort()

min = num[0]
max = num[cnt]

print("%d %d" %(min, max))
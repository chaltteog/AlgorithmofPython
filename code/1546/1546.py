'''
프로그램명 : 1546.py
작성자 : 권혁진
작성일 : 2020-08-26
설명 : 평균
참조 : https://www.acmicpc.net/problem/1546
'''
cnt = (int(input()))
numList = tuple(map(int, input().split()))

r = cnt
maxNum = max(numList)
sumNum = 0

while r > 0:
    r -= 1
    sumNum += numList[r] / maxNum * 100

sumNum = round(sumNum / cnt, 6)
print(sumNum)

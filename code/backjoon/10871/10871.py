'''
프로그램명 : 10871.py
작성자 : 권혁진
작성일 : 2020-02-03
설명 : X보다 작은 수
'''
n, x = map(int, input().split())
numList = list(map(int, input().split()))
out = ''

for i in range(n):
    if numList[i] < x:
        out += str(numList[i]) + ' '

print(out)
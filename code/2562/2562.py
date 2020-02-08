'''
프로그램명 : 2562.py
작성자 : 권혁진
작성일 : 2020-02-08
설명 : 최대
'''
base = []

for i in range(9):
    base.append(int(input()))

maxNum = max(base)

print(maxNum)
print(base.index(maxNum) + 1)
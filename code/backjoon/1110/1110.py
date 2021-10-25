'''
프로그램명 : 1110.py
작성자 : 권혁진
작성일 : 2020-02-08
설명 : 더하기 사이클
'''

base = int(input())
num = base
sumNum = 0

flag = True
rCnt = 0

if num < 10:
    num = "0" + str(num)
else:
    num = str(num)

while flag:
    sumNum = str(int(num[0]) + int(num[1]))
    num = num[1] + sumNum[len(sumNum) - 1]
    rCnt += 1

    if int(num) == base:
        flag = False

print(rCnt)
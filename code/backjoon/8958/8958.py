'''
프로그램명 : 8958.py
작성자 : 권혁진
작성일 : 2020-08-27
설명 : OX퀴즈
참조 : https://www.acmicpc.net/problem/8958
'''
import sys

def count_result_point(result):
    point = 1
    result_point = 0

    for s in result:
        if s == 'O':
            result_point += point
            point += 1
        else:
            point = 1

    return result_point

cnt = int(sys.stdin.readline())
result_point_list = []

while cnt > 0:    
    cnt -= 1
    point = 1
    result_sum = 0

    result = count_result_point(sys.stdin.readline())
    result_point_list.append(result)


for s in result_point_list:
    print(s)

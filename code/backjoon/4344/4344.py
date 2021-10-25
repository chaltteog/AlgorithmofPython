'''
프로그램명 : 4344.py
작성자 : 권혁진
작성일 : 2020-08-28
설명 : 평균은 넘겠지
참조 : https://www.acmicpc.net/problem/4344
'''
import sys

def avg_result_point(result_point_list):
    result_list = list(map(int, result_point_list.split()))

    result_list.reverse()
    cnt = result_list.pop()
    
    result_avg = sum(result_list) / cnt    
    pass_user_cnt = 0

    for num in result_list:
        if num > result_avg:
            pass_user_cnt += 1
        
    return round(pass_user_cnt / cnt * 100, 3)

cnt = int(sys.stdin.readline())
avg_list = []

while cnt > 0:    
    cnt -= 1    
    avg = avg_result_point(sys.stdin.readline())
    avg_list.append(avg)

for i in avg_list:
    print('{:0.3f}%'.format(i))


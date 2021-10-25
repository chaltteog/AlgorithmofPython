'''
프로그램명 : 1065.py
작성자 : 권혁진
작성일 : 2020-09-03
설명 : 한수
참조 : https://www.acmicpc.net/problem/1065
'''

def check_num(num, cnt):        
    if num < 100:
        return cnt + 1

    num_split_list = list(map(int, str(num)))

    if num_split_list[0] - num_split_list[1] == num_split_list[1] - num_split_list[2]:
        return cnt + 1

    return cnt

out = 0
max_cnt = int(input())

while max_cnt > 0:
    out = check_num(max_cnt, out)
    max_cnt -= 1

print(out)
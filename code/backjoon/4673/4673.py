'''
프로그램명 : 4673.py
작성자 : 권혁진
작성일 : 2020-08-30
설명 : 셀프 넘버
참조 : https://www.acmicpc.net/problem/4673
'''

def get_none_self_num(num):
    sum_num = int(num)

    for i in str(num):
        sum_num += int(i)
        
    return sum_num

def generate_self_num_list():
    none_self_num_list = set()
    self_num_list = set(range(1, 10001))

    for num in range(1, 10001):
        none_self_num_list.add(get_none_self_num(num))    

    return self_num_list - none_self_num_list

for out in sorted(generate_self_num_list()):
    print(out)
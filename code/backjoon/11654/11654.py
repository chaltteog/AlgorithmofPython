'''
프로그램명 : 2675.py
작성자 : 권혁진
작성일 : 2020-08-31
설명 : 문자열 반복
참조 : https://www.acmicpc.net/problem/2675
'''

total_cnt = int(input())
output = []

def make_str(input_str):
    cnt, s = map(str, input_str.split())
    output_str = ''

    for charset in s:
        i = int(cnt)

        while i > 0:
            i -= 1
            output_str += charset
        
    return output_str

    
while total_cnt > 0:
    total_cnt -= 1
    output.append(make_str(input()))

for output_str in output:
    print(output_str)
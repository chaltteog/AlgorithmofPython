'''
프로그램명 : 15596.py
작성자 : 권혁진
작성일 : 2020-08-29
설명 : 정수 N개의 합
참조 : https://www.acmicpc.net/problem/15596
'''

def solve(a):
    ans = 0
    
    for num in a:
        ans += num
    
    return ans
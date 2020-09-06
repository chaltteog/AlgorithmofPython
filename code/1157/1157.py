'''
프로그램명 : 1157.py
작성자 : 권혁진
작성일 : 2020-09-06
설명 : 단어 공부
참조 : https://www.acmicpc.net/problem/1157
'''

res_cnt = 0
output = ''

word = str(input()).upper()
char_list = set(word)

for s in char_list:
    cur_cnt = word.count(s)

    if cur_cnt == res_cnt:
        output = '?'
        continue

    if cur_cnt > res_cnt:
        res_cnt = cur_cnt
        output = s

print(output)
        
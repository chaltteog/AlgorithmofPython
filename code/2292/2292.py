'''
프로그램명 : 2292.py
작성자 : 권혁진
작성일 : 2020-09-09
설명 : 벌집
'''
num = int(input())

cnt = 1
size = 6
room_cnt = 1

while num > cnt:
    room_cnt += 1
    cnt += size
    size += 6

print(room_cnt)

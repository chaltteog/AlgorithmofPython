'''
프로그램명 : 10250.py
작성자 : 권혁진
작성일 : 2020-09-15
설명 : ACM 호텔
'''
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = N % H
    room = N // H

    if floor == 0:
        floor = H
        print('{0}{1:02d}'.format(floor, room))
        continue

    if room < W:
        room += 1

    print('{0}{1:02d}'.format(floor, room))

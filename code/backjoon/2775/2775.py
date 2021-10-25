'''
프로그램명 : 2775.py
작성자 : 권혁진
작성일 : 2020-09-11
설명 : 부녀회장이 될테야
참조 : https://www.acmicpc.net/problem/2775
'''

user = int(input())
res_list = list()

for _ in range(user):
    user -= 1

    floor = int(input())
    room = int(input())

    human = [x for x in range(1, room + 1)]
    for _ in range(floor):
        for i in range(1, room):
            human[i] += human[i -1]

    res_list.append(human[room - 1])

for res in res_list:
    print(res)

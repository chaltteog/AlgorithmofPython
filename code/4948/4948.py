'''
프로그램명 : 4948.py
작성자 : 권혁진
작성일 : 2020-09-22
설명 : 베르트랑 공준
참조 : https://www.acmicpc.net/problem/4948
'''

def create_check_prime_list():
    num_len = (123456 * 2)
    prime_list = [True] * (num_len + 1)

    n = int((num_len ** 0.5) + 1)

    for i in range(2, n + 1):
        if prime_list[i]:
            for j in range(2 * i, num_len + 1, i):
                prime_list[j] = False

    return prime_list

prime_list = create_check_prime_list()
while True:
    num = int(input())
    if num == 0: break

    prime_count = 0
    for n in range(num + 1, num * 2 + 1):
        if prime_list[n]:
            prime_count += 1

    print(prime_count)

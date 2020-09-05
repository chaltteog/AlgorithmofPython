'''
프로그램명 : 10809.py
작성자 : 권혁진
작성일 : 2020-09-05
설명 : 알파벳 찾기
참조 : https://www.acmicpc.net/problem/10809
'''

def convert_int_to_str(s):
    if type(s) == int:        
        return str(s)

    return str(-1)


alphabet = list(map(chr, range(97, 123)))
word = input()

for i in range(0, len(word)):
    char = word[i]
    if not char in alphabet:
        continue

    n = alphabet.index(char)    
    alphabet[n] = i

print(' '.join(map(convert_int_to_str, alphabet)))
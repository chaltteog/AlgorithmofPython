'''
프로그램명 : 1316.py
작성자 : 권혁진
작성일 : 2020-09-05
설명 : 그룹 단어 체커
참조 : https://www.acmicpc.net/problem/1316
'''

def check_word_char(word):
    chars = list()
    char_set = set()

    for i in range(0, len(word)):                
        if (word[i - 1] == word[i]) and (i != 0):
            continue
                
        chars.append(word[i])
        char_set.add(word[i])
    
    return len(chars) - len(char_set)

cnt = int(input())
pass_word_cnt = 0

while cnt > 0:
    cnt -= 1    
    word = str(input())

    if check_word_char(word) == 0:
        pass_word_cnt += 1

print(pass_word_cnt)
a = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    dic = {}
    num = 0
    
    for arr in clothes:
        if not arr[1] in dic:
            dic[arr[1]] = []

        dic[arr[1]].append(arr[0])

    for key in dic.keys():
        cnt = len(dic[key]) + 1

        if num == 0:
            num = cnt
            continue

        num *= cnt

    return num - 1

print(solution(a))
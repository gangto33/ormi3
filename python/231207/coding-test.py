# 코딩테스트 연습 - 해시 - 의상

def solution(clothes):
    answer = 1
    dic = {}
    for x, y in clothes:
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 1
            
    for i in dict.values(dic):
        answer *= i + 1

    return answer - 1

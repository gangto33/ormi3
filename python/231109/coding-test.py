# 코딩테스트 연습 - 연습문제 - 귤 고르기

def solution(k, tangerine):
    answer = {}
    size = 0
    for i in tangerine:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
    
    cnt = sorted(dict.values(answer))
    while True:
        k = k - cnt.pop()
        size += 1
        if k <= 0:
            return size

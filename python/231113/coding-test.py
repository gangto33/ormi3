# 코딩테스트 연습 - 월간 코드 챌린지 시즌1 - 쿼드압축 후 개수 세기

def solution(arr):
    half = len(arr) // 2
    
    if sum([sum(i) for i in arr]) == len(arr) ** 2:
        return [0, 1]
    
    elif sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    
    else:
        return [sum(i) for i in zip(*[solution([i[:half] for i in arr[:half]]), solution([i[half:] for i in arr[:half]]), solution([i[:half] for i in arr[half:]]), solution([i[half:] for i in arr[half:]])])]

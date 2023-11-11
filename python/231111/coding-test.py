# 코딩테스트 연습 - 월간 코드 챌린지 시즌1 - 삼각 달팽이

def solution(n):
    answer = []
    start = 1
    last = sum([i for i in range(1, n+1)])
    
    for i in range(1, n+1):
        answer.append([0]*i)
    
    idx = 0
    back = -1
    
    while start != last+1:
        
        for i in range(idx, n):
            if answer[i][idx] == 0:
                answer[i][idx] = start
                start += 1
        idx += 1
        
        for i in range(n):
            if answer[n-1][i] == 0:
                answer[n-1][i] = start
                start += 1
        n -= 1
        
        for i in reversed(range(idx, n)):
            if answer[i][back] == 0:
                answer[i][back] = start
                start += 1
        back -= 1
    
    return sum(answer, [])

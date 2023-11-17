# 코딩테스트 연습 - 연습문제 - 점 찍기

def solution(k, d):
    answer = 0
    limit = d ** 2
    y = 0
    dots = [i for i in range(0, d + 1, k)]
    
    while y <= d:
        start = y ** 2
        end = int((limit - start) ** 0.5)
        
        while dots and dots[-1] > end:
            dots.pop()
        
        answer += len(dots)
        y += k
    
    return answer

# 코딩테스트 연습 - 연습문제 - 마법의 엘리베이터

def solution(storey):
    answer = 0
    stack = [int(i) for i in str(storey)]
    last = stack.pop()
    
    while stack:
        if last == 5:
            answer += 5
            if stack[-1] >= 5:
                last = stack.pop() + 1
            else:
                last = stack.pop()
                
        elif last < 5:
            answer += last
            last = stack.pop()
        
        elif 10 > last > 5:
            answer += 10 - last
            last = stack.pop() + 1
        
        elif last >= 10:
            answer += last - 10
            last = stack.pop() + 1
    
    if last == 10:
        return answer + 1
    
    elif last > 5:
        return answer + (10 - last) + 1
    
    elif last <= 5:
        return answer + last
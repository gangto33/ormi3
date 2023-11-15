# 코딩테스트 연습 - 탐욕법(Greedy) - 큰 수 만들기

def solution(number, k):
    answer = []
    
    for i in number:
        while answer and answer[-1] < i and k != 0:
            answer.pop()
            k -= 1
            
        answer.append(i)
        
    if k != 0:
        answer = answer[:-k]
        
    return "".join(answer)

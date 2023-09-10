# 코딩테스트 연습 - 연습문제 - 줄 서는 방법

def solution(n, k):
    answer = []
    facto = [1]
    num_list = []
    k = k - 1
    
    for i in range(1, n+1):
        num_list.append(i)
        facto.append(facto[-1] * i)
        
    while n != 0:
        num, k = divmod(k, facto[n - 1])
        answer.append(num_list.pop(num))
        n = n - 1
    
    return answer
# 코딩테스트 연습 - 연습문제 - 디펜스 게임

import heapq
from collections import deque

def solution(n, k, enemy):
    answer = 0
    deq = deque(enemy)
    heap = []
    
    while deq and n >= 0:
        i = -deq.popleft()
        heapq.heappush(heap, i)
        n += i
        if n < 0 and k > 0:
            k -= 1
            n -= heapq.heappop(heap)
        elif n < 0 and k == 0:
            return answer
        
        answer += 1
    
    return answer

# 코딩테스트 연습 - 스택/큐 - 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    deq = deque(truck_weights)
    bridge = deque()

    while deq:
        while weight - deq[0] >= 0:
            truck = deq.popleft()
            weight -= truck
            bridge.append(truck)
            answer += 1
            if not deq:
                return answer + bridge_length

        while len(bridge) < bridge_length:
            bridge.append(0)
            answer += 1

        out = bridge.popleft()
        weight += out
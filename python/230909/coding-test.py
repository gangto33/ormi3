# 코딩테스트 연습 - 깊이/너비 우선 탐색(DFS/BFS) - 네트워크

def solution(n, computers):
    answer = 0
    stack = []
    visited = set()
    
    for i in range(n):
        if i not in visited:
            answer += 1
            stack.append(i)
            visited.add(i)
            
            while stack:
                network = stack.pop()
                for i in range(n):
                    if computers[network][i] == 1 and i not in visited:
                        stack.append(i)
                        visited.add(i)
    
    return answer
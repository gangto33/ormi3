# 코딩테스트 연습 - 연습문제 - 무인도 여행

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    check = [[False] * m for _ in range(n)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not check[i][j]:
                stack = [(i, j)]
                food = 0
                while stack:
                    x, y = stack.pop()
                    if check[x][y]:
                        continue
                        
                    check[x][y] = True
                    food += int(maps[x][y])
                    
                    for mx, my in move:
                        if 0 <= x + mx < n and 0 <= y + my < m:
                            if maps[x + mx][y + my] != 'X':
                                stack.append((x + mx, y + my))
                answer.append(food)
    
    if answer:
        return sorted(answer)
    
    else:
        return [-1]
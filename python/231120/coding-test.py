# 코딩테스트 연습 - 연습문제 - 가장 큰 정사각형 찾기
 
def solution(board):
    
    for i in range(1, len(board)):
        for x in range(1, len(board[i])):
            if board[i][x] != 0:
                board[i][x] = min(board[i-1][x-1], board[i-1][x], board[i][x-1]) + 1
            
    return max([max(i) for i in board]) ** 2

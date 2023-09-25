# 샌드위치 포장

def solution(data):
    stack = []
    cnt = 0
    
    for i in data:
        stack.append(i)
        if i == 1 and stack[-5:] == [1, 2, 3, 4, 1]:
            stack = stack[:-5]
            cnt += 1
    
    return cnt
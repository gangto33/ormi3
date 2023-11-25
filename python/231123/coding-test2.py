# 코딩테스트 연습 - 연습문제 - 혼자 놀기의 달인

def solution(cards):
    answer = 0
    check = [True] * len(cards)
    stack = []
    num_list = []
    
    for i in range(len(cards)):
        if not check[i]:
            continue
            
        else:
            num_list.append(cards[i])
            check[i] = False
            num = cards[i]
        
            while check[num-1]:
                check[num-1] = False
                num_list.append(cards[num-1])
                num = cards[num-1]
            
            stack.append(len(num_list))
            num_list.clear()
    
    if len(stack) <= 1:
        return 0
    else:
        max_num = max(stack)
        stack.remove(max_num)
        return max_num * max(stack)

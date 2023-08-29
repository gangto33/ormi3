def solution(begin, target, words):
    answer = float('inf')
    length = len(begin) - 1
    words = set(words)
    
    if target not in words:
        return 0
    
    stack = [(0, begin, words)]
    
    while stack:
        cnt, start, group = stack.pop()
        
        if start == target:
            answer = min(answer, cnt)
        
        for word in group:
            check = list(filter(lambda x: x[0] == x[1], zip(start, word)))
            
            if len(check) == length:
                stack.append((cnt + 1, word, group - set([word])))
    
    return answer
# 코딩테스트 연습 - 월간 코드 챌린지 시즌2 - 괄호 회전하기

def solution(s):
    answer = 0
    correct = [['(', ')'], ['[', ']'], ['{', '}']]
    stack = []
    s = list(s)
    for i in range(len(s)):
        for x in s:
            stack += [x]
            if stack[-2:] in correct:
                del stack[-2:]
        if len(stack) == 0:
            answer += 1
        stack.clear()
        s.append(s.pop(0))
    return answer
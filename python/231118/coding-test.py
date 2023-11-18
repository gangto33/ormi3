# 코딩테스트 연습 - 연습문제 - 땅따먹기

def solution(land):
    land = land[::-1]
    start = land.pop()
    while land:
        full_score = max(start)
        for i in range(len(start)):
            if i == start.index(full_score):
                land[-1][i] = land[-1][i] + sorted(start)[2]
            else:
                land[-1][i] = land[-1][i] + full_score

        start = land.pop()

    return max(start)

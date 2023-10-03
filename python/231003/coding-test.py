# 코딩테스트 연습 - 연습문제 - 테이블 해시 함수

def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        S_i = sum(s % (i+1) for s in data[i])
        answer ^= S_i
    
    return answer
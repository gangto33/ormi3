# 코딩테스트 연습 - Summer/Winter Coding(~2018) - 배달

def solution(N, road, K):
    answer = 0
    dp = [False, 0] + [500000 for i in range(N-1)]
    visit = [1]
    
    while len(visit) != 0:
        visit.clear()
        
        for i in road:
            if dp[i[0]] != 500000:
                if dp[i[1]] > dp[i[0]] + i[2]:
                    dp[i[1]] = dp[i[0]] + i[2]
                    visit.append(i[1])
            if dp[i[1]] != 500000:
                if dp[i[0]] > dp[i[1]] + i[2]:
                    dp[i[0]] = dp[i[1]] + i[2]
                    visit.append(i[0])
                    
    for i in dp[1:]:
        if i <= K:
            answer += 1
    
    return answer

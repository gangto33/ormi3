# 코딩테스트 연습 - 연습문제 - 롤케이크 자르기

def solution(topping):
    answer = 1
    big = {}
    young = {}

    for i in topping:
        if i in big:
            big[i] = big[i] + 1
        else:
            big[i] = 1

    while len(big) != len(young):
        a = topping.pop()
        if not topping:
            return 0

        if a in young:
            young[a] = young[a] + 1
        else:
            young[a] = 1

        big[a] = big[a] - 1

        if big[a] == 0:
            del big[a]

    while len(big) == len(young):
        a = topping.pop()
        if a in young:
            young[a] = young[a] + 1
        else:
            return answer

        big[a] = big[a] - 1

        if big[a] == 0:
            return answer

        answer += 1

    return answer
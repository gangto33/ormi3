# 코딩테스트 연습 - 탐욕법(Greedy) - 구명보트

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    for i in people:
        while i + people[-1] <= limit:
            i = i + people.pop()
        answer += 1
    return answer

# 코딩테스트 연습 - 연습문제 - 할인 행사 

def solution(want, number, discount):
    answer = 0
    want_list = []
    for i in range(len(want)):
        want_list += [want[i]] * number[i]
    
    for i in range(len(discount)):
        if i+sum(number) <= len(discount):
            a = discount[i:i+sum(number)]
            for x in want_list:
                if x in a:
                    a.remove(x)
                else:
                    break
            if not a:
                answer += 1
                
    return answer

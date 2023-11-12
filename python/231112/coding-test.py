# 코딩테스트 연습 - 월간 코드 챌린지 시즌2 - 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    while numbers:
        number = numbers.pop()
        if number % 4 != 3:
            answer.append(number + 1)
        else:
            b_num = bin(number)[2:]
            if '0' not in b_num:
                answer.append(int('10' + b_num[1:], 2))
            else:
                b_num = list(b_num)[::-1]
                idx = b_num.index('0')
                b_num[idx-1], b_num[idx] = '0', '1'
                answer.append(int(''.join(b_num[::-1]),2))
                
    answer.reverse()        
    
    return answer

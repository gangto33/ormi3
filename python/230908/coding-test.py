# 코딩테스트 연습 - 2021 KAKAO BLIND RECRUITMENT - 신규 아이디 추천

def solution(new_id):
    answer = ''
    
    # 소문자 치환 (1단계)
    new_id = new_id.lower()
    
    for s in new_id:
        # 두 개 이상의 마침표 치환 (3단계)
        if len(answer) != 0 and s == '.' and answer[-1] == '.':
            continue
        
        # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 고르기 (2단계)
        elif s.isalnum() or s == '-' or s == '_' or s == '.':
            answer += s
            
    # 양 끝의 '.' 제거 (4단계)
    answer = answer.strip('.')
    
    # 빈 문자열일 경우 "a" 대입 (5단계)
    if not answer:
        answer += 'a'
    
    # 길이가 16이상일 경우 나머지 문자 제거, 끝의 마침표 제거 (6단계)
    answer = answer[:15].rstrip('.')
    
    # 길이가 2 이하일 경우, 길이가 3이 되도록 마지막 문자를 이어붙이기. (7단계)
    return answer if len(answer) > 2 else answer + (answer[-1] * (3 - len(answer)))

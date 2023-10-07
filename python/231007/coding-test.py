# 코딩테스트 연습 - 연습문제 - 광물 캐기

def solution(picks, minerals):
    answer = 0
    dia, iron, stone = picks
    piro = []

    for mineral in minerals:
        if mineral == "diamond":
            piro.append(25)
        elif mineral == "iron":
            piro.append(5)
        elif mineral == "stone":
            piro.append(1)

    piro = piro[:sum(picks)*5]
    cnt = []

    while piro:
        cnt.append(piro[:5])
        piro = piro[5:]
    cnt.sort(key = lambda x: sum(x))

    while cnt and dia != 0:
        dia -= 1
        answer += len(cnt.pop())
    while cnt and iron != 0:
        iron -= 1
        answer += sum(map(lambda x: x // 5 if x > 1 else 1, cnt.pop()))
    while cnt:
        answer += sum(cnt.pop())

    return answer
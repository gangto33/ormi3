# 문제 1 : 주어진 리스트 data = [{"이름": "길동", "수학": 3, "과학": 93}, {"이름": "춘향", "수학": 33, "과학": 11}, {"이름": "철수", "수학": 94, "과학": 67}]에서 평균점수가 가장 높은 학생에 이름을 출력하세요.

data = [{"이름": "길동", "수학": 3, "과학": 93}, {"이름": "춘향", "수학": 33, "과학": 11}, {"이름": "철수", "수학": 94, "과학": 67}]

best_name = '이름'
best_score = float('-inf')

for i in range(len(data)):
    score = sum([j for j in data[i].values() if type(j) != str]) / (len(data[i]) - 1)
    if best_score < score:
        best_score, best_name = score, data[i]['이름']

print(best_name)

# 문제 2 : 주어진 사전 grades = {"Tom": 87, "Jerry": 95, "Mickey": 70}의 모든 값을 5점씩 증가시키고 결과를 출력하세요.

grades = {"Tom": 87, "Jerry": 95, "Mickey": 70}
for grade in grades:
    grades[grade] += 5

print(grades)

# 문제 3 : 주어진 문자열 s = "apple banana apple cherry banana cherry apple"에서 가장 자주 등장하는 단어를 출력하세요.

s = "apple banana apple cherry banana cherry apple"

dic = {}

for fruit in s.split():
    if fruit in dic:
        dic[fruit] += 1
    else:
        dic[fruit] = 1

print(max(dic, key=dic.get))
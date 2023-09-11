# 문제1

x = 3
y = 5
result = (isinstance(x, int) and isinstance(y, int)) and (x + y) # 여기에 논리연산자를 더 붙여 두 수를 더하는 코드를 만들어보세요.
print(result) # 8이 출력되어야 합니다.

# 문제2

print('hello' < 'hell o') # 'o' 와 ' '의 유니코드 비교가 우선이기에 ('hello' > 'hell o') == True 입니다.
print([10, 20, 30] < [10, 19, 100]) # 위와 동일하게 20과 19의 비교가 우선입니다.
print(10 % 3.3 == 0.1) # 실수의 부동소수점 문제로 인해 생기는 오류입니다. 양쪽에 10읍 곱하고 계산 후 10을 나눠주면 해결할 수 있습니다.

# 문제3

email2 = 'abc@gmail.com' # gmail
email3 = 'abc@naver.com' # naver
email4 = 'abc@weniv.co.kr' # weniv
email5 = 'li.cat@weniv.co.kr' # weniv

email2.split('@')[-1].split('.')[0]
email3.split('@')[-1].split('.')[0]
email4.split('@')[-1].split('.')[0]
email5.split('@')[-1].split('.')[0]
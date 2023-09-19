# 문제2(class 쓰레드)
# 하나의 숫자에 제곱근을 구하는 함수 sqrt_number(num)이 있었을 때
# 자체 예외 NegativeNumberError를 정의하세요. 이 예외는 음수가 입력될 때 발생하도록 합니다.
# 사용자로부터 숫자를 입력 받아 그 숫자의 제곱근을 반환하는 함수를 작성하세요.
# 입력된 숫자가 음수이면 NegativeNumberError를 발생시키고 
# "음수의 제곱근은 계산할 수 없습니다."라는 메시지를 출력하세요.

class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__('음수의 제곱근은 계산할 수 없습니다.')

def sqrt_number(num):
    if num >= 0:
        return num ** (1/2)

    else:
        raise NegativeNumberError

# 문제3(class 쓰레드)
# 사용자로부터 인덱스 값을 입력 받아서 리스트 ["apple", "banana", "cherry"]에서 
# 해당 인덱스의 값을 출력하는 함수를 작성하세요.
# 사용자가 범위를 벗어난 인덱스를 입력하면 "리스트의 범위를 벗어났습니다."라는 메시지를 출력하세요.

def get_item(num):
    item_list = ["apple", "banana", "cherry"]
    try:
        return item_list[int(num)]

    except:
        return "리스트의 범위를 벗어났습니다."

num = input('인덱스 값을 입력해 주세요.: ')
get_item(num)
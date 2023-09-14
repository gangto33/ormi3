# .py파일로 작성해서 실행해보세요.
import os

while True:
    userinput = input('>')
    if userinput == 'pwd':
        # print('현재 위치 출력')
        # print('\\'.join(__file__.split('\\')[:-1]))
        print(os.getcwd())
    elif userinput == 'dir' or userinput == 'ls':
        # print('현재 폴더에 폴더와 파일명 출력')
        print(os.listdir(os.getcwd()))
    elif userinput == 'exit':
        print('안녕히가세요.')
        break

# class 연습문제

# 아래 기본 data를 기반으로 문제를 풀어주세요.
data = [
  {
    "_id": "fd7e9a0f-e77b-436a-B781-119b66033d49",
    "index": "1",
    "name": "나주헌",
    "gender": "여성",
    "age": "43"
  },
  {
    "_id": "8ec6eabb-160a-41e4-A3de-cd33aff0b281",
    "index": "2",
    "name": "엄루다",
    "gender": "남성",
    "age": "22"
  },
  {
    "_id": "bcf804f7-0452-4c31-B9d1-20cc2d38490b",
    "index": "3",
    "name": "형유환",
    "gender": "남성",
    "age": "31"
  }
]

# 문제 1 gender, age값을 추출해보세요. 아래 양식처럼 추출하시면 됩니다. 가능하면 map을 사용해주세요.

list(map(lambda x: {"gender": x.get("gender"), "age": x.get("age")},data))

# 문제 2 User라는 class를 만들어 해당 데이터를 관리해주세요. 아래처럼 저장되어야 합니다. 
# 다만 꼭 변수 이름이 user_1...user_n 일 필요는 없습니다.
# 저장양식: '[user_1, user_2, user_3]'

class User:
    def __init__(self, value):
        self.value = value
        self._id = value["_id"]
        self.index = value["index"]
        self.name = value["name"]
        self.gender = value["gender"]
        self.age = value["age"]

user_1 = User(data[0])
user_2 = User(data[1])
user_3 = User(data[2])

data_list = [user_1, user_2, user_3]

# 문제 3 BankAccount 클래스를 생성하세요. 이 클래스는 owner(계좌주 이름), balance(잔액) 속성을 가져야 합니다.
# 이 클래스는 deposit(amount) (입금) 및 withdraw(amount) (출금) 메서드를 가져야 합니다. 
# 단, 출금 시 잔액보다 큰 금액을 출금하려고 하면 "잔액 부족" 메시지를 출력해야 합니다.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return '입금 되었습니다.'

        else:
            return '입금할 수 없는 금액입니다.'
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return '출금 되었습니다.'
        
        elif self.balance <= amount:
            return '잔액이 부족합니다.'
        
        else:
            return '출금할 수 없는 금액입니다.'

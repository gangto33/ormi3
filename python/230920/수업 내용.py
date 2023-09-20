# 문제1
# 다음과 같이 동작하는 제너레이터 함수 fibonacci(n)를 완성하세요. 
# 주어진 숫자 n까지의 피보나치 수열을 반환합니다.

def fib(n):
    pre = 1
    next = 1
    count = 0
    while True:
        temp = pre + next
        yield pre
        pre, next = next, temp
        count += 1
        if count == n:
            break

for i in fib(5):
    print(i)

'''
출력
1
1
2
3
5
'''

# 문제2
# 주어진 함수의 실행 시간을 측정하여 출력하는 데코레이터 time_it를 작성하세요. 
# (힌트: time 모듈의 time() 함수를 사용하세요.)

import time

def time_it(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{end_time - start_time:.4f}s")
    return wrapper

@time_it
def main():
    def fib(n):
        pre = 1
        next = 1
        count = 0
        while True:
            temp = pre + next
            yield pre
            pre, next = next, temp
            count += 1
            if count == n:
                break

    for i in fib(20):
        print(i)

main()
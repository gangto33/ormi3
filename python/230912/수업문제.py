# 문제 1

def is_palindrome(s):
    # 코드를 작성하세요.
    s = list(filter(lambda x: x.isalnum(), s.lower()))
    half = len(s) // 2
    return s[:half] == list(reversed(s[-half:]))

print(is_palindrome("level"))  # 결과: True
print(is_palindrome("python")) # 결과: False

# 문제 2

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# 여기에 코드를 작성하세요.
numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(numbers)  # 결과: [3, 5, 7, 9]
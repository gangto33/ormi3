'''동물 클래스 Animal을 만들어주세요. Dog와 Cat 클래스를 각각 정의하십시오. 

Animal 클래스는 name 속성을 가집니다. 이 클래스는 make_sound 메서드를 갖고 있습니다.

Dog와 Cat 클래스는 Animal 클래스를 상속받는 클래스입니다.Dog 클래스의 make_sound 메서드는 "멍멍!"을, Cat 클래스의 make_sound 메서드는 "야옹!"을 출력하도록 재정의하세요.

더 완성도 높은 클래스를 만들어보세요. 추가 속성이나 메서드 작성 가능합니다.'''

class Animal:

    def __init__(self, name):
        self.name = name
  
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("멍멍!")

class Cat(Animal):

    def make_sound(self):
        print("야옹!")

a = Cat("호두")
a.name
a.make_sound()

'''Person이라는 기본 클래스를 만들어주세요. Person 클래스는 이름과 나이라는 두 개의 속성과 소개하기라는 메서드를 가지며,
이 메서드는 "Hello World!, 제 이름은 [이름]이고 제 나이는 [나이]살 입니다."라는 메시지를 출력합니다.

Person 클래스를 상속받는 Student 클래스를 정의하십시오. Student 클래스는 추가적으로 학년 속성을 가집니다.
Student 클래스에서 소개하기 메서드를 오버라이드하여 "Hello World!, 제 이름은 [이름]이고 제 나이는 [나이]살 입니다. 그리고 저는 [학년]학년입니다. "라는 메시지를 출력하도록 만드세요.'''

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def 소개하기(self):
        print(f"Hello World!, 제 이름은 {self.name}이고 제 나이는 {self.age}살 입니다.")

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def 소개하기(self):
        print(f"Hello World!, 제 이름은 {self.name}이고 제 나이는 {self.age}살 입니다. 그리고 저는 {self.grade}학년입니다.")


a = Person('강토', 27)
a.소개하기()
a = Student('강토', 27, 3)
a.소개하기()
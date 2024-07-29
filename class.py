# 객체를 만들기 위한 청사진
# 첫 글자는 무조건 대문자이여야 한다. = PascalCase
class User:
    pass


# class 를 이용한 User 만들기
user_1 = User()
user_1.id = "001"
user_1.username = "Jack"


# 객체를 생성할때 속성을 설정하지 않아도 속성이 생성된다.
print(user_1.username)



# __init__ : 생성자
class Car:
    def __init__(self):
        # initialise attributes




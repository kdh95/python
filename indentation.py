# 파이썬에서는 들여쓰기가 매우매우매우 중요하다.
# 함수를 정의후에 들여쓰기 한 부분은 모두 함수에 포함된다.
def my_function():
    print("Hello") # 함수에 포함된다,
    print("World") # 함수에 포함된다.


print("Bye") # 함수에 포함되지 않는다.

# 만약 다른 코드블록들이 있다면 좀 더 복잡해진다.
# 예를 들어 if,elif, else 문을 생각해보자
def my_function():
    sky = "grey" # 공백 4칸 == 탭1번
    if sky == 'clear':
        print("blue") # 공백 8칸 == 탭2번
    elif sky == "cloudy"
        print("grey")
    print("Hello")

print("World")

# 파이썬 공식문서에는 스페이스를 사용하라고 되어있다.


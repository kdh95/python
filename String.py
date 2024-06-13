# 줄바꿈해서 print 해보기
print("Hello World!\nHello World!")

# String 결합해서 출력해보기
print("Hello" + "World!") # 가운데 space는 없다.

# HelloWorld! 가운데에 space 넣기
print("Hello " + "World!")
print("Hello" + " World!")
print("Hello" + " " + "World!")


# 문자열 생성
x = "Hello World"
y = 'Hello World'

# 이스케이프 문자
# 1. \n : 문자열 내에서 줄을 바꿀 때 사용
# 2. \t : 문자열 안에서 몇 칸 간격을 벌릴 때 사용
# 3. \\ : \ 자체를 문자로 표현할 때 사용
# 4. \' : ' 자체를 문자로 표현할 떄 사용
# 5. \" : " 자체를 문자로 표현할 때 사용


# 문자열의 인덱스
# 인덱스는 0부터 시작하며 문자열은 인덱스를 가지고 있다.
x = 'Hello World!'
print("문자열의 첫번째 문자 : " + x[0])

# -1 인덱스
# 파이썬은 음수 인덱스를 지원하며 -1은 가장 마지막 인덱스를, -2는 마지막에서 두 번째 인덱스를 나타낸다.
print("제일 마지막 문자 : " + x[-1])
print("제일 첫번째 문자 : " + x[-11]) # Hello World! 가 공백 포함 11자리 이기 때문에
# 만약 문자열의 범위(=길이)를 벗어나면 에러가 발생한다.

# 문자열 슬라이싱
# [시작인덱스 : 끝인덱스] : 시작인덱스부터 끝인덱스 -1에 해당하는 문자열 부분을 추출한다.
# 시작인덱스나 끝인덱스가 생략되어 있으면 0부터 혹은 끝까지로 간주하고 추출한다.

# 다른 내장함수들도 존재한다.
# upper(), lower(), replace(), split()
# strip(), lstrtp(), rstrip() 이건 각각 양쪽 공백, 왼쪽 공백, 오른쪽 공백을 지우는 함수
# format(), find(), count()
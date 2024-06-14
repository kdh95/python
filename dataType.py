# Float
3.123131

# Boolean
True
False

# String
"Hello"

# Integer
123

# Large integer
123_456_789


# 이건 에러 발생 String 을 int 로 변환할 수 없음
num_char = len(input("what is your name?"))
#print("Your name has " + num_char + " characters.")

new_num_char = type(num_char)
# 형식 변경
str(num_char)

print("Your name has " + new_num_char + " characters.")

# 아래 예제 생각해보기
a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))



# 연습문제
two_digit_number = input()
# Try hitting Run Code to see the data type
# input : 39 => output => 3 + 9 = 12
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
print(first_num + second_num)




# 연산
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# 연산 우선순위
# 1. ()
# 2. **
# 3. * / /
# 4. + / -
print(3 * 3 + 3 / 3 - 3)



# 연습문제 BMI 계산하기
# BMI 계산법 => BMI = wieght(kg) / hieght^2(m^2)
height = input()
weight = input()

weight_num = int(weight)
height_num = float(height)

bmi = weight_num / height_num ** 2

bmi = int(bmi)

print(bmi)



# 반올림
print(round(8 / 3))
# 소수점 2번째 자리에서 반올림하기
print(round(8 / 3, 2))

# 버림하기
print(8 // 3) # 정수로 치환할 필요 없이 정수값을 조회 가능

# 연속 연산
a = 4 / 2
a /= 2
print(a)


# f-String
score = 0
print(f"your score is {score}")



# 연습문제 팁 계산
print("Welcome to the tip calculator")
input_bill = float(input("What was the total bill?"))
input_percentage = int(input("What persentage tip would you like to give? 10, 12 or 15?"))
input_person_num = int(input("How many people to split the bill?"))


result = "{:.2f}".format(int(input_percentage / 100 * input_bill + input_bill) / input_person_num)


print(f"Each person should pay: {result}")




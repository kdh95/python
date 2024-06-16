print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Operator
# >
# <
# >=
# <=
# ==
# !=

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7")
    elif age > 12:
        print("Please pay $14")
    else:
        print("Please pay $18")
else:
    print("Sorry, you have to grow taller before you can ride.")



# 연습문제 윤년 계산하기
# 4로 나누어 떨어지는 해는 윤년으로 한다.
# 연수가 4,100 으로 나누어 떨어지는 해는 평년으로 한다.
# 4, 100, 300 으로 나누어 떨어지는 해는 윤년으로 둔다.
# Which year do you want to check?
year = int(input())

if year % 4 == 0 and year % 100 == 0 and year % 300 == 0:
  print("Leap year")
elif year % 4 == 0 and year % 100 == 0:
  print("Not leap year")
elif year % 4 == 0:
  print("Leap year")
else:
  print("Not leap year")


# if / elif / else
#
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# A, B, C 중에 하나만 실행된다.



# Multiple if
#
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C
# 조건이 모두 일치하면 A, B, C 모두 실행될 수 있다.
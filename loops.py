# For Loop with Lists
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits: # 명령어를 원하는 만큼 반복해준다.
    print(fruit)




# For Loop with Range
for number in range(1, 10): # 10은 포함하지 않는다.
    print(number)

for number in range(1, 11, 3): # 3씩 증가한다.
    print(number)



# 연습문제
# FizzBuzz
# 규칙 : 원형으로 서서 1부터 시작해 돌아가면서 한 명씩 숫자를 외친다.
# 3으로 나뉘는 숫자를 만나는 순간 "피즈"를 외친다. 5로 나뉘는 숫자를 만난 경우 "버즈"를 외친다,
# 3 과 5 모두로 나뉘는 숫자를 만나면 "피즈버즈"를 외쳐야 한다.
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)





# While 반복문
# while something_is_true:
#     do something








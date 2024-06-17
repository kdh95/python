# 무작위화는 무엇일까?
# 일정 수준의 예측 불가능성이 존재하는 컴퓨터 프로그램을 개발할 때 매우 중요하다.
# 가장 대표적인 카테고리는 게임이 있을 것이다. 예를 들어 테트리스 게임을 플레이할때 블록이 예측 불가능하게 나타나는것을 생각하면 된다.
# 하지만 컴퓨터는 상당히 결정적인 기계인데 어덯게 난수를 생성할 수 있을까?
# 파이썬에는 난수를 생성하는 다양한 모듈아 존재한다.

import random
import my_module # 나만의 모듈을 만들 수 있다.

random_integer = random.randint(1, 10) # 1과 10을 포함하여 무작이 정수를 생성해준다.
print(random_integer)


random_float = random.random() # 1을 제외하고 0.0 ~ 1.0 사이에 난수를 생성해준다.
print(random_float)

# 만약 0부터 5사이에 난수가 필요하면 어떻게 할까?
random_float2 = random.random()

random_float2 * 5 # 이렇게 5를 곱하면 해결된다. 0.000000..... - 4.999999......

print(my_module.pi)




love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")





# List는 데이터 자료구조이다. 파이썬에서 데이터를 체계화하고 저장하는 방식을 말한다.
# 서로 관계성이 있는 데이터 그룹을 저장해야할때 사용한다.
# 대괄호 한 쌍 안에 항목을 저장한다.
# 문자열이나 숫자, 불리언 집합을 저장할 수 있다.
fruits = ['apple', 'banana']
# 리스트에는 순서가 있다. 순서가 보존되기 때문에 순서를 사용할 수 있다.
print(fruits[0])
# 음수 인덱스를 넣으면 뒤에서 부터 접근이 가능하다.
print(fruits[-1]) # 가장 마지막에 있는 인덱스에 접근

# 리스트 마지막에 값을 추가하고 싶으면
# append() 함수를 사용하면 된다.
fruits.append("watermelon")

print(fruits[-1])

# 이것 말고도 다양한 리스트 관련 함수가 존재한다.
# 2개이상 값을 추가하려면 extend() 함수를 사용한다.


# 리스트를 사용할때 가장 흔하게 접하는 에러는 index out of range 오류이다.
# 만약 50개의 항목이 리스트에 있다면 마지막 인덱스의 번호는 49이다.
# 이때 인덱스 50에 접근하려고 하면 에러가 발생한다.
# 리스트의 len() 을 변수에 저장하고
# list[len()] 으로 접근하려고 하면 에러가 발생한다. 그렇기 때문에 -1을 해주어야 한다.




# 연습문제 가위바위보 하기

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])


if user_choice == computer_choice:
    print("It's a draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")








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








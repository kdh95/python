# 김도한 퀴즈


print("안녕하세요. 김도한 퀴즈에 오신것을 환영합니다. 5개 이상 맞추면 선물이 있습니다.")
correct_answer = 0

height = int(input("김도한의 키는 몇 cm 일까요?"))

if height == 175:
    print("정답입니다!!!")
    correct_answer += 1
else:
    print("이것도 모르냐?")

weight = int(input("김도한의 몸무게는 몇 kg 일까요?"))

if weight == 95:
    print("정답입니다!!")
    correct_answer += 1
else:
    print("진짜 싦망입니다.")

blood_type = input("김도한의 혈액형은 무엇일까요?")

if blood_type == 'O':
    print("정답입니다.!!!")
    correct_answer += 1
else:
    print("바보가 분명하군...")


favorite_food = input("김도한이 가장 좋아하는 음식은 무엇일까요?")

if favorite_food == "국밥":
    print("당신은 나를 사랑한는군요")
    correct_answer += 1
else:
    print("당신은 나를 좋아하지 않아요...")


my_love = input("김도한이 사랑하는 여자는?")

if my_love == "박뚱딴지천방지축어리둥절빙긍빙글돌아가는":
    print("정답입니다. 당신은 정말 천재에요!!")
    correct_answer += 1
else:
    print("틀렸습니다... 정답은 : '박뚱딴지천방지축어리둥절빙긍빙글돌아가는' 입니다.")


if correct_answer < 5:
    print(f"당신은 {correct_answer}개를 맞췄네요 김도한에 대해서 모르는군요... 조금 더 분발하도록 해요")
else:
    print(" 사랑합니다...")
